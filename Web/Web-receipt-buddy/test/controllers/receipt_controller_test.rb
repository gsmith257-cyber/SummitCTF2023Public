require "test_helper"

class ReceiptControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get receipt_index_url
    assert_response :success
  end
end
