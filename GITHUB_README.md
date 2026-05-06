# ⚡ برنامج التسعير الكهربائي
# Electrical Pricing App

A professional Arabic web application for tracking and managing electrical product prices across multiple stores in Kuwait.

## 🎯 Features

### 📊 Dashboard
- Real-time KPI cards (Total Products, Active Stores, Average Price, Price Range)
- Colorful revenue distribution chart
- Monitored stores table with statistics
- Gradient background and vibrant colors

### 🔍 Product Search
- Advanced search with multiple filters
- Filter by product name
- Filter by store/shop
- Filter by price range (min/max)
- Real-time results

### 📋 Materials Table (جدول المواد)
- Select products from dropdown
- Enter quantities
- Auto-calculate unit prices from database
- Auto-calculate total (Quantity × Unit Price)
- Add/remove rows dynamically
- **Export to Excel** (CSV format)
- **Export to Word** (coming soon)
- Running total at bottom

### 📦 Catalog (كتالوج)
- Full product inventory
- Store information
- Current prices (د.ك)
- Stock availability with color badges

### 💾 Historical Database
- Complete product history
- Store statistics over time
- Price trends
- Archive information

### 📈 Interactive Charts
- Store distribution (percentage bars)
- Price range distribution
- Toggleable chart types
- Percentage display

### 🏪 Stores & Management
- All monitored stores
- Product count per store
- Average prices per store
- Status indicators

### 🔐 Admin Panel
- Secure admin authentication (password protected)
- **Monthly data update limit** (for legal compliance)
- One-time daily update maximum
- Complete audit log of all updates
- Update frequency settings (daily/weekly/monthly/quarterly)
- Legal compliance notice

### ⚙️ Settings
- Light/Dark mode toggle
- Font selection (IBM Plex, Cairo, Tajawal)
- Theme customization

## 📱 Access

- **Web**: `http://localhost:8889/pricing-app.html`
- **Streamlit**: Deploy via Streamlit Cloud
- **Mobile**: Fully responsive - works on all devices

## 🛠️ Technologies

- **Frontend**: React 18 + Babel (JSX transpilation)
- **Styling**: CSS3 with CSS Variables for theming
- **Data Format**: JSON
- **Deployment**: Streamlit Cloud
- **Language**: Arabic (RTL) & English

## 📁 File Structure

```
electrical-pricing-app/
├── pricing-app.html          # Main React application
├── products_all.json         # Product database
├── app.py                    # Streamlit wrapper
├── requirements.txt          # Python dependencies
├── GITHUB_README.md          # This file
└── .gitignore               # Git ignore rules
```

## 🚀 Deployment Steps

### 1️⃣ Local Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/electrical-pricing-app.git
cd electrical-pricing-app

# Install Python dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### 2️⃣ Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New App"
4. Select your GitHub repository
5. Set main file: `app.py`
6. Click "Deploy"

### 3️⃣ Access on Phone

Once deployed, you'll get a public URL:
```
https://your-username-electrical-pricing-app.streamlit.app
```

Open this URL on your phone's browser to access the app!

## 📊 Data Format

**products_all.json structure:**
```json
[
  {
    "store": "دخيل الجسار",
    "name": "كيبل كهربائي NYY 3×2.5mm",
    "price": 1.85,
    "url": "https://...",
    "timestamp": "2026-05-01 12:55:01",
    "currency": "KD"
  }
]
```

## 🔐 Legal & Safety

✅ **Compliance Features:**
- Monthly data update limit (ethical scraping)
- Admin-only manual data updates
- Full audit log of all changes
- Respects target services' policies
- No automated scraping

## 💡 Usage Tips

### Product Search
1. Go to "المنتجات" (Products) page
2. Enter product name in search box
3. Optionally filter by store or price range
4. Results update in real-time

### Create Materials Table
1. Go to "جدول المواد" (Materials Table)
2. Click "اختر منتج" (Choose Product)
3. Select a product from dropdown
4. Enter quantity
5. Price auto-populates
6. Total calculates automatically
7. Click "📊 تصدير Excel" to export

### Update Data
1. Go to "🔐 الإدارة" (Admin Panel)
2. Enter password: `admin2024`
3. Click "🔄 تحديث البيانات الآن" (Update Data Now)
4. Confirm the update
5. View update history in log

## 🎨 Design Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Mode**: Eye-friendly night theme
- **RTL Support**: Full Arabic right-to-left layout
- **Vibrant Colors**: Modern gradient backgrounds
- **Professional Typography**: Arabic fonts (IBM Plex, Cairo, Tajawal)
- **Accessibility**: High contrast, readable fonts

## 📞 Support

For issues or questions:
1. Check GitHub Issues
2. Review README documentation
3. Test on different browsers/devices

## 📄 License

Open source - feel free to use and modify

## 👨‍💻 Author

Created with Claude AI

---

## التعليمات بالعربية

### الميزات الرئيسية:
- ✅ تتبع أسعار المنتجات الكهربائية
- ✅ بحث متقدم مع فلترة
- ✅ جدول مواد مع حسابات تلقائية
- ✅ تصدير إلى Excel
- ✅ لوحة تحكم آمنة للإداريين
- ✅ وضع ليلي
- ✅ دعم العربية الكامل

### الخطوات:
1. اذهب إلى Streamlit Cloud
2. انسخ رابط المشروع من GitHub
3. اضغط Deploy
4. افتح الرابط على هاتفك!

---

**Last Updated**: May 2026
**Version**: 1.0.0
**Status**: ✅ Production Ready
