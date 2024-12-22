class Router {
  constructor() {
    this.routes = {
      home: "pages/home.html",
      products: "pages/products.html",
      account: "pages/account.html",
      admin: "pages/admin.html",
    };

    // Xử lý routing khi hash thay đổi
    window.addEventListener("hashchange", () => this.handleRoute());
    window.addEventListener("load", () => this.handleRoute());
  }

  async handleRoute() {
    let hash = window.location.hash.slice(2) || "home";
    const contentDiv = document.getElementById("main-content");

    try {
      // Load nội dung từ file html tương ứng
      const response = await fetch(this.routes[hash]);
      const content = await response.text();
      contentDiv.innerHTML = content;

      // Cập nhật trạng thái active cho menu
      document.querySelectorAll(".sidebar a").forEach((link) => {
        if (link.getAttribute("href") === "#/" + hash) {
          link.classList.add("active");
        } else {
          link.classList.remove("active");
        }
      });
    } catch (error) {
      console.error("Error loading page:", error);
      contentDiv.innerHTML = "<h2>Error loading page</h2>";
    }
  }
}

// Khởi tạo router
const router = new Router();
