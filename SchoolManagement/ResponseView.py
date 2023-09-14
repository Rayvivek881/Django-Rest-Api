from rest_framework.response import Response

class ResponseView():
  def get_success_response(self, data, status_code=200):
    return Response({
      'status': True,
      'message': 'Success',
      'data': data
    }, status=status_code)
  
  def get_error_response(self, message, status_code=400):
    return Response({
      'status': False,
      'message': message
    }, status=status_code)