drf_social_oauth2_context_processors = [
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]

drf_social_oauth2_default_authentication_classes = [
    # django-oauth-toolkit < 1.0.0
    # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    # django-oauth-toolkit >= 1.0.0
    'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    'drf_social_oauth2.authentication.SocialAuthentication',
]

AUTHENTICATION_BACKENDS = [
   # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # Google  OAuth2
    'social_core.backends.google.GoogleOAuth2',
    # Google OpenID Integration OAuth2
    'drf_social_oauth2.backends.GoogleIdentityBackend',
    # GitHub OAuth2
    'social_core.backends.github.GithubOAuth2',
    # Instagram OAuth2
    'social_core.backends.instagram.InstagramOAuth2',
    # Linked OpenID
    'drf_social_oauth2.backends.LinkedInOpenIDUserInfo',
    # drf_social_oauth2
    'drf_social_oauth2.backends.DjangoOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
]

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '<your app id goes here>'
SOCIAL_AUTH_FACEBOOK_SECRET = '<your app secret goes here>'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your app id goes here>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your app secret goes here>'

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
# GitHub configuration
SOCIAL_AUTH_GITHUB_KEY = '<your app id goes here>'
SOCIAL_AUTH_GITHUB_SECRET = '<your app secret goes here>'

# Instagram configuration
SOCIAL_AUTH_INSTAGRAM_KEY = '<your app id goes here>'
SOCIAL_AUTH_INSTAGRAM_SECRET = '<your app secret goes here>'
SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}

# LINKEDIN configuration
SOCIAL_AUTH_LINKEDIN_OPENIDCONNECT_KEY = 'key goes here'
SOCIAL_AUTH_LINKEDIN_OPENIDCONNECT_SECRET = 'secret goes here'
