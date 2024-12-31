from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .serializers import CryptoDataSerializer
from .scraping import scrape_crypto_data

@api_view(['POST'])
def get_crypto_data(request):
    date_str = request.data.get('date')
    if not date_str:
        return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Convert the date string to the required format
    try:
        date = datetime.fromisoformat(date_str)
        formatted_date = date.strftime('%Y-%m-%d')
    except ValueError:
        return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        coins_data = scrape_crypto_data(formatted_date)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Serialize the data
    serializer = CryptoDataSerializer(coins_data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)