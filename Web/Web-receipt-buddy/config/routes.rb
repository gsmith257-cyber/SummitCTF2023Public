Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  root "receipt#index"

  # Post request to /api/receipt
  post "/api/receipt" => "receipt#create"

  # Create route to receipt test 
  get "/api/test" => "receipt#test"
end
