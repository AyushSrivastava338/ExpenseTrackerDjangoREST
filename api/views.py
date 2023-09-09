from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import date, timedelta
from django.db.models import Sum
from .serializer import ExpenseSerializer, UserSerializer
from .models import Expense

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/endpoints',
            'method': 'GET',
            'body': None,
            'description': 'Returns all the available end points on the server'
        },
        {
            'Endpoint': '/api/expenses',
            'method': 'GET',
            'body': None,
            'description': 'Returns all the expenses of the user'
        },
        {
            'Endpoint': '/api/expenses/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns the expense of the user with given id'
        },
        {
            'Endpoint': '/api/expenses',
            'method': 'POST',
            'body': {
                'name': 'type(String)',
                'amount': 'type(String)'
            },
            'description': 'Creates an expense for the user'
        },
        {
            'Endpoint': '/api/endpoints',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes the user expense with given id'
        }
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        print(request.user)
        return Response({
            'status': 200,
            'message': 'GET METHOD CALLED'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'POST METHOD CALLED'
        })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def expenses(request):
    if request.method == 'GET':
        all_expenses = Expense.objects.filter(user=str(request.user)).all()
        serializer = ExpenseSerializer(all_expenses, many=True)
        return Response(
            serializer.data
        )
    elif request.method == 'POST':
        try:
            data = request.data
            data['user'] = str(request.user)
            serializer = ExpenseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                all_expenses = Expense.objects.filter(user=str(request.user)).all()
                all_serializer = ExpenseSerializer(all_expenses, many=True)
                return Response({
                    'status': True,
                    'message': 'Success',
                    'data': all_serializer.data
                })

            print(serializer.data)
            return Response({
                'status': False,
                'message': 'Failure',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
        return Response({
            'status': False,
        })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_expense(request, id):
    expense = Expense.objects.filter(user=str(request.user), id=id).delete()
    # serializer = ExpenseSerializer(expense)
    return Response({
        'status': True,
        'message': 'Expense Deleted'
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sum_of_last_7_days(request):
    sums_last_7_days = []

    # Calculate sums for each of the last 7 days
    for i in range(7):
        start_date = date.today() - timedelta(days=i)
        end_date = start_date + timedelta(1)

        total_expenses = Expense.objects.filter(
            user=request.user,
            timestamp__gte=start_date,
            timestamp__lt=end_date
        ).aggregate(Sum('amount'))['amount__sum'] or 0  # Default to 0 if there are no expenses

        sums_last_7_days.append(total_expenses)

    return Response({'expenses_last_7_days': sums_last_7_days})

