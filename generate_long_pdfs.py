import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_long_pdf(filename, title, chapters):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'C:\\Windows\\Fonts\\arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:\\Windows\\Fonts\\arialbd.ttf'))
        font_name = 'Arial'
        font_bold = 'Arial-Bold'
    except Exception as e:
        font_name = 'Helvetica'
        font_bold = 'Helvetica-Bold'
        
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontName=font_bold, fontSize=18, spaceAfter=20, alignment=1)
    heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], fontName=font_bold, fontSize=14, spaceAfter=10, spaceBefore=15)
    normal_style = ParagraphStyle('CustomNormal', parent=styles['Normal'], fontName=font_name, fontSize=12, spaceAfter=8, leading=16)

    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    
    for chapter_title, paragraphs in chapters:
        story.append(Paragraph(chapter_title, heading_style))
        for para in paragraphs:
            story.append(Paragraph(para, normal_style))
            
    doc.build(story)

if __name__ == '__main__':
    out_dir = "mock_pdfs"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. LONG IT DOCUMENT
    it_chapters = []
    for i in range(1, 21):
        paragraphs = [
            f"Đây là phần mô tả chi tiết cho chương {i}. Hệ thống AI Chatbot cần phải tuân thủ nghiêm ngặt các quy định về bảo mật theo tiêu chuẩn ISO 27001.",
            f"Trong quá trình vận hành mô-đun {i}, các kỹ sư phần mềm phải kiểm tra log định kỳ mỗi 4 giờ. Bất kỳ dấu hiệu bất thường nào (ví dụ: memory spike, CPU overload) đều phải được báo cáo ngay cho trưởng nhóm.",
            f"Cấu hình mạng của cụm server số {i} bao gồm 3 lớp firewall: firewall ngoại vi, lớp ứng dụng, và firewall cơ sở dữ liệu. Tất cả lưu lượng truy cập qua cổng 443 đều được giám sát thời gian thực bằng hệ thống IDS/IPS.",
            f"Theo khảo sát tháng {i}/2026, lượng người dùng đồng thời cao nhất ghi nhận được là {i * 1500} CCU. Do đó, hệ thống auto-scaling trên AWS sẽ tự động thêm EC2 instance nếu mức sử dụng RAM vượt quá 85%.",
            f"Quy trình deploy phiên bản {i}.0: Bước 1 - Đẩy code lên nhánh main; Bước 2 - Chạy CI/CD qua Jenkins; Bước 3 - Kiểm thử tự động với Selenium; Bước 4 - Chờ phê duyệt của QA; Bước 5 - Triển khai lên Production bằng Kubernetes."
        ]
        it_chapters.append((f"Chương {i}: Quy trình và Bảo mật hệ thống phần {i}", paragraphs))
        
    create_long_pdf(f"{out_dir}/IT_04_Tai_Lieu_Huong_Dan_Bao_Mat_Chuyen_Sau.pdf", "SỔ TAY HƯỚNG DẪN BẢO MẬT VÀ VẬN HÀNH HỆ THỐNG", it_chapters)

    # 2. LONG ACCOUNTING DOCUMENT
    acc_chapters = []
    for i in range(1, 21):
        paragraphs = [
            f"Chính sách tài chính điều {i}: Tất cả các khoản chi tiêu vượt quá mức {i * 50} triệu VNĐ đều phải thông qua phê duyệt của Giám đốc Tài chính (CFO) và được lưu vết trên hệ thống ERP.",
            f"Quản lý hóa đơn chứng từ trong quý {i%4 + 1}: Kế toán viên có trách nhiệm scan và lưu trữ hóa đơn điện tử vào thư mục dùng chung trước ngày 5 hàng tháng. Mã số thuế đối tác cần được kiểm tra chéo với dữ liệu từ Tổng cục Thuế.",
            f"Theo nghị định {i}/2026/NĐ-CP, thuế suất thuế giá trị gia tăng (VAT) cho nhóm dịch vụ công nghệ thông tin được duy trì ở mức 10%. Các công ty phần mềm cần khai báo rõ nguồn thu từ bán license và doanh thu từ dịch vụ bảo trì.",
            f"Kiểm toán nội bộ đợt {i}: Yêu cầu các bộ phận lập bảng kê khai tài sản cố định bao gồm: Laptop, máy chủ, bàn ghế văn phòng và bản quyền phần mềm có giá trị lớn hơn 30 triệu đồng.",
            f"Dự báo dòng tiền (Cashflow) tháng {i}: Dựa trên số liệu lịch sử, khoản thu hồi công nợ dự kiến từ khách hàng doanh nghiệp là {i * 2.5} tỷ đồng. Khoản chi cho quỹ lương và bảo hiểm xã hội chiếm tỷ trọng lớn nhất, khoảng 45% tổng chi phí."
        ]
        acc_chapters.append((f"Điều {i}: Chính sách và Quy định Tài chính số {i}", paragraphs))

    create_long_pdf(f"{out_dir}/KeToan_04_Chinh_Sach_Tai_Chinh_Tong_Hop.pdf", "CẨM NANG CHÍNH SÁCH TÀI CHÍNH VÀ KẾ TOÁN QUẢN TRỊ 2026", acc_chapters)
