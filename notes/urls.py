from django.urls import path
from .views import NoteList, CreateNote, NoteDetail

urlpatterns = [
    path("notes/", NoteList.as_view(), name="notes_list"),
    path("notes/new/", CreateNote.as_view(), name="create_note"),
    path("notes/<int:pk>/", NoteDetail.as_view(), name="note_detail"),
]
