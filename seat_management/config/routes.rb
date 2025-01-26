Rails.application.routes.draw do
  root "seats#index"
  post "seats/update", to: "seats#update"  

end