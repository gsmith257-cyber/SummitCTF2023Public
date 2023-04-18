# flag: summitCTF{w4tch_Out_4_th0s3_p3skY_SSRFs_in_UR_R3ceipts_lma0}

class ReceiptController < ApplicationController
  def index
  end

  def is_number? string
    true if Float(string) rescue false
  end

  def create
    # Get POST data and parse JSON
    json_data = JSON.parse(request.body.read)

    # Pull out the data
    business = json_data["business"]
    name = json_data["name"]
    email = json_data["email"]
    price = json_data["price"]
    method = json_data["method"]
    comments = json_data["comments"]
    fees = json_data["fees"]
    addr_line_one = json_data["addressLineOne"]
    addr_line_two = json_data["addressLineTwo"]
    item = json_data["item"]

    # Check if any fields are blank
    if business.blank? || name.blank? || email.blank? || price.blank? || method.blank? || addr_line_one.blank? || addr_line_two.blank? || item.blank?
      render json: { error: "Please enter the required fields." }, status: :bad_request
      return
    end
    
    # If fees is blank, set it to 0
    if fees.blank?
      fees = 0.00
    end

    # Ensure the s
    if !is_number?(price) || !is_number?(fees)
      render json: { error: "Please enter a valid number for price and fees." }, status: :bad_request
      return
    end

    # Convert the price and fees to a decimal
    price = price.to_f
    fees = fees.to_f
    
    WickedPdf.config = {
      enable_local_file_access: true
    }

    # Generate PDF using WickedPDF
    pdf = WickedPdf.new.pdf_from_string(
      render_to_string(template: 'layouts/pdf', locals: { business: business, name: name, email: email, price: price, comments: comments, fees: fees, addr_line_one: addr_line_one, addr_line_two: addr_line_two, method: method, item: item })
    )

    send_data pdf, filename: "receipt.pdf", type: "application/pdf", disposition: "inline"
  end
end
