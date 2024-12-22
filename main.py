from flask import Flask, render_template,redirect, url_for, request, flash
from supabase import create_client

app = Flask(__name__, static_folder="static")
app.secret_key = "sell_source_shin_shinsad" 
SQL_url = "https://mlfmjhmkfdshkmsgrxcp.supabase.co"
SQL_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1sZm1qaG1rZmRzaGttc2dyeGNwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzQ4MzQ4MTgsImV4cCI6MjA1MDQxMDgxOH0.eg0mEHY1QjEU9Tj12TcNiFvvDmQUAsos0b-Sh_iQ01M"
supabase = create_client(SQL_url, SQL_key)
# save_device = supabase.table("devices").select("*").execute()
    

@app.route('/')
def home():
    # Danh sách sản phẩm mẫu
    products = [
        {
            "id": 1,
            "name": "Giao diện HTML bán hàng",
            "price": "500,000 VND",
            "description": "Mẫu giao diện bán hàng chuyên nghiệp với HTML và CSS.",
            "image": "source1.jpg",
            "type": "HTML"
        },
        {
            "id": 2,
            "name": "Quản lý công việc với Python",
            "price": "1,000,000 VND",
            "description": "Ứng dụng quản lý công việc hoàn chỉnh với Flask.",
            "image": "source2.jpg",
            "type": "Python"
        }
    ]
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    # Chi tiết sản phẩm (giả lập)
    product_details = {
        "id": id,
        "name": "Giao diện HTML bán hàng",
        "price": "500,000 VND",
        "description": "Mẫu giao diện bán hàng chuyên nghiệp với HTML và CSS.",
        "image": "source1.jpg",
        "source_code": "<!DOCTYPE html>\n<html>\n<head>\n<title>Shop</title>\n</head>\n<body>\n<h1>Chào mừng đến với cửa hàng của chúng tôi!</h1>\n</body>\n</html>",
        "type": "HTML"
    }
    return render_template('product.html', product=product_details)

@app.route('/demo/<int:id>')
def demo(id):
    return render_template('demo.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(f"Login attempt - Email: {email}, Password: {password}")
        
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print(f"Registration attempt - Username: {username}, Email: {email}, Password: {password}")

        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('register'))

        try:
            save_requests_SQL = supabase.table("user").insert({
                "username": username,
                "email": email,
                "password": password,
            }).execute()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for('register'))

    return render_template('register.html')
if __name__ == "__main__":
    app.run(debug=True)
