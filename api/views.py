from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ExpenseSerializer
from .models import Expense
from django.utils.dateparse import parse_datetime

# Create your views here.

@api_view(['GET'])
def getRoutes():
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

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'GET METHOD CALLED'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'POST METHOD CALLED'
        })


@api_view(['GET'])
def get_all_expenses(request):
    all_expenses = Expense.objects.all()
    serializer = ExpenseSerializer(all_expenses, many=True)
    return Response({
        'status': True,
        'message': 'Expenses fetched',
        'data': serializer.data
    })

@api_view(['POST'])
def post_expense(request):
    try:
        data = request.data

        serializer = ExpenseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Success',
                'data': serializer.data
            })

        print(serializer.data)
        return Response({
            'status': False,
            'message': 'Success',
            'data': serializer.errors
        })

    except Exception as e:
        print(e)
    return Response({
        'status': False,
    })