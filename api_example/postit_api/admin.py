from django.contrib import admin
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
# Register your models here.

class AlbumInline(admin.TabularInline):
    model = Album
    readonly_fields = ('id',)
    can_delete = False
    extra = 0  # išjungia papildomas tuščias eilutes įvedimui

class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'band_name')
    inlines = [AlbumInline]
    fieldsets = (
        (None, {'fields': ('band_name',)}),
    )

class SongInline(admin.TabularInline):
    model = Song
    readonly_fields = ('id',)
    can_delete = False
    extra = 0  # išjungia papildomas tuščias eilutes įvedimui

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'band_id', 'album_name')
    inlines = [SongInline]
    fieldsets = (
        (None, {'fields': ('album_name',)}),
    )

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_id' , 'song_name', 'duration')
    fieldsets = (
        (None, {'fields': ('song_name','duration',)}),
    )


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)
