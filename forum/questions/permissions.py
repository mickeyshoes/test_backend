from rest_framework import permissions

# 수정, 삭제와 같은 작업을 할 경우 해당 객체의 저자가 로그인을 한 본인인지 확인 하기 위한 permission
class CheckObjectOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.writer # 질문과 댓글의 저자의 필드와 비교할 것이기 떄문에 writer