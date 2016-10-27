#here is a secret file, which need 2 key,
#mapquest_key is develop key for mapquest api
#mapbox_key is develop key for mapbox api
class Secret():
    def __init__(self):
      self.mapquest_key = "0QFqsOaM2IuBdUQWnAi6EZHD3GwedpjK"
      self.mapbox_key = "pk.eyJ1IjoieXUzNHBvIiwiYSI6ImNpdW5xb3J3cTAwMHUydGw4djlrbjBxNXEifQ._euk9gk-k8sI4ux0c7G-3Q";

    def get_mapbox_key(self):
        return self.mapbox_key

    def get_mapquest_key(self):
        return self.mapquest_key

