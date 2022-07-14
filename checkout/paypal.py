import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AbYtMu__0L4xpe-tXJfEUfUXqP3vCZEReaFUWD6hlJ2sD2UfeEuSaBXPD9vyxGU_XeM2F-GqzFYWQlkm"
        self.client_secret = "ECHdOxiP_uDszf1JHcAV7GfLbaeL04bcVEaldwkrQkvuZxOXAjsGpnEBPLpsEBpOV5WEKXE0PGBnoOEF"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
