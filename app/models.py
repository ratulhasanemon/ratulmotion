from django.db import models


class Project(models.Model):
    title       = models.CharField(max_length=200, verbose_name="Project Title")
    subtitle    = models.CharField(max_length=200, blank=True, verbose_name="Subtitle (e.g. Artistic direction)")
    video_file  = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="Upload Video File")
    video_url   = models.URLField(blank=True, verbose_name="Vimeo URL (optional)", help_text="e.g. https://player.vimeo.com/video/824804225")
    is_wide     = models.BooleanField(default=False, verbose_name="Wide card (full width)?")
    is_active   = models.BooleanField(default=True, verbose_name="Show on site?")
    order       = models.PositiveIntegerField(default=0, verbose_name="Display order")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def get_video_src(self):
        """Return uploaded file URL or Vimeo URL"""
        if self.video_file:
            return ('file', self.video_file.url)
        elif self.video_url:
            return ('vimeo', self.video_url)
        return (None, None)
