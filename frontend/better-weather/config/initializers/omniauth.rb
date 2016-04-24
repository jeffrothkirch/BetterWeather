Rails.application.config.middleware.use OmniAuth::Builder do
  provider :instagram, 'd9901cd57c944807890120a35451363a', '35fe3011dc6c4ae2af8d8910fc1b30d9',
      provider_ignores_state: true
end