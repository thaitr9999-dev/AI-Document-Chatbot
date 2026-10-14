import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_pdf(filename, title, content_paragraphs, table_data=None):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Register Arial font for Vietnamese support
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'C:\\Windows\\Fonts\\arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:\\Windows\\Fonts\\arialbd.ttf'))
        font_name = 'Arial'
        font_bold = 'Arial-Bold'
    except Exception as e:
        print(f"Warning: Could not load Arial font, falling back to default. Vietnamese characters might not display correctly. Error: {e}")
        font_name = 'Helvetica'
        font_bold = 'Helvetica-Bold'
        
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontName=font_bold,
        fontSize=16,
        spaceAfter=14
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=12,
        spaceAfter=10,
        leading=16
    )

    story = []
    
    # Add title
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    
    # Add paragraphs
    for para in content_paragraphs:
        story.append(Paragraph(para, normal_style))
    
    # Add table if provided
    if table_data:
        story.append(Spacer(1, 12))
        t = Table(table_data)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), font_bold),
            ('FONTSIZE', (0,0), (-1,0), 12),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
            ('FONTNAME', (0,1), (-1,-1), font_name),
            ('GRID', (0,0), (-1,-1), 1, colors.black)
        ]))
        story.append(t)
        
    doc.build(story)


if __name__ == '__main__':
    out_dir = "mock_pdfs"
    os.makedirs(out_dir, exist_ok=True)
    
    # --- IT Documents ---
    
    it_doc1_content = [
        "Tài liệu này mô tả kiến trúc của hệ thống AI Chatbot phiên bản 2.0.",
        "Hệ thống bao gồm 3 thành phần chính: Frontend (ReactJS), Backend (Spring Boot), và AI Engine (Python/LLM).",
        "Dữ liệu được mã hóa ở trạng thái nghỉ bằng thuật toán AES-256. Giao tiếp giữa các dịch vụ sử dụng gRPC để tối ưu hiệu suất.",
        "Điều 1.1: Mọi API endpoint phải yêu cầu xác thực bằng JWT Token.",
        "Điều 1.2: Dữ liệu log không được chứa thông tin nhạy cảm của người dùng (PII)."
    ]
    create_pdf(f"{out_dir}/IT_01_Kien_Truc_He_Thong.pdf", "TÀI LIỆU KIẾN TRÚC HỆ THỐNG AI CHATBOT", it_doc1_content)
    
    it_doc2_content = [
        "Biên bản họp báo cáo sự cố sập server ngày 15/08/2026.",
        "Thời gian bắt đầu sự cố: 14:00 ngày 15/08/2026.",
        "Thời gian khắc phục xong: 16:30 ngày 15/08/2026.",
        "Nguyên nhân: Tràn bộ nhớ do memory leak trong module xử lý file PDF của người dùng.",
        "Hành động khắc phục: Cập nhật thư viện phân tích PDF, thiết lập giới hạn dung lượng file upload tối đa là 50MB."
    ]
    create_pdf(f"{out_dir}/IT_02_Bao_Cao_Su_Co_Server.pdf", "BIÊN BẢN SỰ CỐ HỆ THỐNG 15/08/2026", it_doc2_content)
    
    it_doc3_content = [
        "Kế hoạch triển khai hệ thống quản lý tài liệu nội bộ.",
        "Giai đoạn 1 (01/09/2026 - 15/09/2026): Triển khai môi trường UAT và kiểm thử nội bộ.",
        "Giai đoạn 2 (16/09/2026 - 30/09/2026): Triển khai production cho phòng Hành chính - Nhân sự.",
        "Dưới đây là danh sách phân bổ server:"
    ]
    it_table3 = [
        ["Tên Server", "Cấu hình", "IP Nội bộ", "Chức năng"],
        ["APP-SRV-01", "8 vCPU, 16GB RAM", "192.168.1.10", "Backend Spring Boot"],
        ["DB-SRV-01", "16 vCPU, 32GB RAM", "192.168.1.20", "PostgreSQL Database"],
        ["AI-SRV-01", "16 vCPU, 64GB RAM, 1x A100", "192.168.1.30", "LLM Inference Engine"]
    ]
    create_pdf(f"{out_dir}/IT_03_Ke_Hoach_Trien_Khai.pdf", "KẾ HOẠCH TRIỂN KHAI INFRASTRUCTURE", it_doc3_content, it_table3)
    
    # --- Accounting Documents ---
    
    acc_doc1_content = [
        "Báo cáo tổng hợp doanh thu tháng 7 năm 2026 của chi nhánh Hà Nội.",
        "Tổng doanh thu đạt 15.5 tỷ VNĐ, vượt 12% so với mục tiêu đề ra (13.8 tỷ VNĐ).",
        "Chi phí vận hành và marketing chiếm 4.2 tỷ VNĐ.",
        "Lợi nhuận ròng sau thuế đạt 9.8 tỷ VNĐ, tăng trưởng 5% so với cùng kỳ năm ngoái."
    ]
    acc_table1 = [
        ["Hạng mục", "Doanh thu (Tỷ VNĐ)", "Tỷ trọng (%)"],
        ["Bán lẻ phần mềm", "8.5", "54.8%"],
        ["Dịch vụ bảo trì", "5.0", "32.2%"],
        ["Đào tạo và tư vấn", "2.0", "13.0%"]
    ]
    create_pdf(f"{out_dir}/KeToan_01_Bao_Cao_Doanh_Thu_T7.pdf", "BÁO CÁO DOANH THU THÁNG 7/2026", acc_doc1_content, acc_table1)
    
    acc_doc2_content = [
        "Quy định mới về thanh toán công tác phí năm 2026, áp dụng từ ngày 01/09/2026.",
        "Điều 1: Định mức tiền ăn ca cho nhân viên công tác trong nước là 300,000 VNĐ/ngày.",
        "Điều 2: Tiền thuê phòng nghỉ không vượt quá 1,000,000 VNĐ/đêm đối với cấp nhân viên, và 2,000,000 VNĐ/đêm đối với cấp quản lý.",
        "Điều 3: Mọi hóa đơn thanh toán phải là hóa đơn điện tử hợp lệ và có xuất mã số thuế của công ty (MST: 0101234567)."
    ]
    create_pdf(f"{out_dir}/KeToan_02_Quy_Dinh_Cong_Tac_Phi.pdf", "QUY ĐỊNH THANH TOÁN CÔNG TÁC PHÍ NĂM 2026", acc_doc2_content)
    
    acc_doc3_content = [
        "Biên bản nghiệm thu và thanh lý hợp đồng cung cấp thiết bị máy tính cho phòng kế toán.",
        "Bên A: Công ty TNHH AI Document Chatbot.",
        "Bên B: Công ty CP Máy Tính ABC.",
        "Ngày nghiệm thu: 18/08/2026.",
        "Bên B đã bàn giao đầy đủ số lượng thiết bị theo hợp đồng số 123/HĐKT-2026. Số tiền Bên A cần thanh toán đợt cuối cho Bên B là: 125,000,000 VNĐ (Bằng chữ: Một trăm hai mươi lăm triệu đồng chẵn)."
    ]
    acc_table3 = [
        ["STT", "Tên thiết bị", "Số lượng", "Đơn giá (VNĐ)", "Thành tiền (VNĐ)"],
        ["1", "Laptop Dell Latitude 7420", "5", "20,000,000", "100,000,000"],
        ["2", "Màn hình Dell Ultrasharp 24", "5", "5,000,000", "25,000,000"],
        ["", "TỔNG CỘNG", "", "", "125,000,000"]
    ]
    create_pdf(f"{out_dir}/KeToan_03_Nghiem_Thu_Thanh_Ly.pdf", "BIÊN BẢN NGHIỆM THU VÀ THANH LÝ HỢP ĐỒNG", acc_doc3_content, acc_table3)
    
    print(f"Hoàn thành! Các file đã được lưu trong thư mục: {os.path.abspath(out_dir)}")
