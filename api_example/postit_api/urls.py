from django.urls import path
from .views import AlbumReviewList, BandList, AlbumList, AlbumReviewCommentList, AlbumReviewDetail, \
    AlbumReviewLikeCreat, \
    AlbumReviewCommentDetail, SongList, UserCreate

urlpatterns = [
    path('bands/', BandList.as_view(), name='bands'),
    path('bands/<int:pk>/albums/', AlbumList.as_view(), name='albums'),
    path('bands/<int:pk>/albums/<int:id>/songs/', SongList.as_view(), name='songs'),
    path('albumreviews/', AlbumReviewList.as_view(), name='albumreviews'),
    path('albumreviews/<int:pk>/', AlbumReviewDetail.as_view(), name='albumreviewdetails'),
    path('albumreviews/<int:pk>/comments/', AlbumReviewCommentList.as_view(), name='albumreviewcomments'),
    path('albumreviews/<int:pk>/comments/<int:id>/', AlbumReviewCommentDetail.as_view(), name='albumreviewcommentdetails'),
    path('albumreviews/<int:pk>/likes/', AlbumReviewLikeCreat.as_view(), name='albumreviewlikes'),
    path('signup/', UserCreate.as_view()),
]