class SeatsController < ApplicationController
  protect_from_forgery with: :null_session

  before_action :authenticate_api_key, only: [:update]

  def index
    @seats = Seat.all # 全ての座席情報を取得
  end
  
  def update
    data = params[:data]

    # すべての座席を満席にする
    Seat.update_all(is_occupied: true)
  
    # リストに含まれる識別子に対応する座席を空席に更新
    Seat.where(identifier: data).update_all(is_occupied: false)
  
    Rails.logger.info("Seats updated successfully.")
  
    head :ok # 空のレスポンスを返す
  end

  private

  def authenticate_api_key
    api_key = request.headers['X-API-KEY']
    expected_api_key = 'c9b3d1e8a97b0fd340ed9db4e75d6d74a6bb6a1f7f0e1c2e0ff35d547774276d'
    unless api_key == expected_api_key
      render status: :forbidden, json: { error: 'Forbidden' }
    end
  end
end