Chương 1: TỔNG QUAN VỀ TTNT
1. Lịch sử phát triển của TTNT
1930: Alan Turing nghĩ ra TTNT.
1956: J.Mc Carthy, M. Minsky, A. Newell, Shannon. Simon,… đưa ra khái niêm “trí tuệ nhân tạo”
1960: Đại học MIT ra đời NNLT LISP( ngôn ngữu đầu tiên dùng cho TTNT).
1961: Thuật ngữ lần đầu sd tại đại học MIT
Thập kỉ 1960s: thời kì lạc quan của ttnt: các ctr trò chơi, chứng minh tự động, tính tích phân bất định, điều khiển robot,..
1970-1971: ttnt bế tác do hạn chế về bộ nhớ và tốc độ tính toán của mt.
1972-1980: ttnt ra đời vấn đề xử lí nntn, biểu diễn tri thức và giải quyết vấn đề, nnlt LISP, Prolog, các hệ chuyên gia,...
1980: ttnt ứng dụng trong thiết bị dân dụng( máy giặt, máy ảnh,..), ra đời hệ thống nhận dạng, xử lý ảnh, xử lý tiếng nói,..
1990-nay: tập trung nghiên cứu: cơ chế suy diễn, ttnt phân tạo, các mô hình tác tử,..
2. Tiền đề cho sự phát triển của TTNT.
Tiền đề: Logic hình thức, tâm lý học nhận thức, tự động hoá,..
Ứng dụng: hệ chuyên gia, Robot xử lý tri thức
3. Trí tuệ con người.
Định nghĩa 1: Theo Alan Turing: Trí tuệ là những gì có thể được đánh giá thông qua các trắc nghiệm thông minh
Định nghĩa 2: Theo từ điển Webster: Trí tuệ là sự phản ứng 1 cách thích hợp trước những tình huống mới thông qua việc hiệu chỉnh hành vi 1 cách thích đáng
Định nghĩa 3: Theo các nhà tâm lý học: Trí tuệ con người được tiến hành thông qua 4 thao tác cơ bản
4. Trí tuệ máy.
Chưa có định nghĩa mà chỉ có dấu hiệu nhận biết trí tuệ máy là TTNT
Các khả năng của TTNT
• Khả năng học
• Khả năng mô phỏng hành vi của con người
• Khả năng trừu tượng hoá, tổng quát hoá và suy diễn
• Khả năng tự giải thích hành vi
• Khả năng thích nghi với tình huống mới trong đó có khả năng thu nạp tri thức và dữ liệu
• Khả năng xử lý các biểu diễn hình thức như các ký hiệu tượng trưng, danh sách
• Khả năng sử dụng các tri thức heuristic (mẹo, kinh nghiệm)
• Khả năng xử lý các thông tin không đầy đủ, không chính xác
5. Trí tuệ nhân tạo.
Trí tuệ nhân tạo (AI - Artificial Intelligence): Là một ngành của khoa học máy tính liên quan đến việc tự động hóa các hành vi thông minh
TTNT: Phải được đặt trên những nguyên lý, lý thuyết vững chắc, có khả năng ứng dụng được. Những nguyên lý này bao gồm:
• Các cấu trúc dữ liệu để biểu diễn tri thức
• Các thuật toán để áp dụng cho những tri thức đó • Các ngôn ngữ và kỹ thuật lập trình để cài đặt
6. Một số lĩnh vực ứng dụng của TTNT.
Các phương pháp tìm kiếm lời giải: Hệ chuyên gia, Hệ thống giải trí, Hệ thống xử lý tiếng nói, Xử lý ngôn ngữ tự nhiên, Hệ thống nhận dạng,  Lập kế hoạch và người máy (robot),  Máy học,  Các mô hình nơ ron (mạng nơ ron và giải thuật di truyền),...

Chương 2: TÁC TỬ THÔNG MINH
1. Tác tử và môi trường.
Khái niệm: Một tác tử (agent) là bất cứ thứ gì cảm nhận môi trường quanh nó thông qua các cảm biến và tác động trở lại môi trường thông qua bộ kích hoạt
Đa tác tử (multi-agent): Là một hệ thống gồm nhiều tác tử (agent) độc lập, tương tác với nhau để giải quyết một vấn đề chung hoặc nhiệm vụ nào đó
2. Đặc điểm của tác tử.
Cho đích cần đạt và các tri thức sẵn có, tác tử cần:
Sử dụng thông tin thu được từ các quan sát mới để cập nhật lại tri thức của nó
Trên cơ sở tri thức của nó, thực thi hành động nhằm đạt được mục tiêu đề ra trong thế giới của nó
Một tác tử được gọi là tự trị nếu hành vi được xác định bởi kinh nghiệm của chính bản thân nó (với khả năng học và thích nghi)
3. Các yếu tố cần xem xét khi thiết kế tác tử.
Khi thiết kế một tác tử, cần phải xem xét 4 yếu tố:  Performance measure(hàm đo hiệu năng),  Enviroment(môi trường),  Actuator(bộ kích hoạt),  Sensor( cảm biến)=> PEAS
4. Đặc điểm của môi trường: 5 đặc điểm
Tính quan sát được.
Tính xác định được.
Tính động.
Tính liên tục hay rời rạc.
Là đơn tác tử hay rời rạc.
5. Phân loại tác tử: 5 loại tác tử
Tác tử phản xạ đơn giản: Tác tử hành động chỉ dựa trên trạng thái hiện tại, không xét đến quá khứ
Tác tử phản xạ có trạng thái: Tác tử lưu các trái thái bên trong (internal states) dựa trên chuỗi percept, phản ánh ít nhất một vài khía cạnh không quan sát được của môi trường.
Tác tử hướng mục đích: Có 3 dạng đích->Đích khiến tác tử phải suy luận về tương lai hoặc các trạng thái khác. Có thể không có hành động nào đưa đến đích.
Tác tử hướng lợi ích: thực hiện hành động sao cho có lợi nhất về lâu dài, đem lại lợi ích lớn, có thể suy luận về các nhiệm vụ có nhiều đích, về sự xung đợt giữa các đích và về các tình huống không chắc chắn.
Tác tử với khả năng học.


Chương 3: GIẢI QUYẾT VẤN ĐỀ BẰNG TÌM KIẾM
1. GQVĐ và khoa học Trí tuệ nhân tạo
GQVĐ là 1 quá trình tìm lời giải thông qua các cách
Phương pháp tính toán nhờ 1 giải thuật
Tìm kiếm heuristic
Dùng phương pháp THỬ và SAI
Dùng phương pháp NHÁNH - CẬN
2. GQVĐ của con người
Mô hình xử lý thông tin gồm 3 thành phần: Hệ thống cảm nhận, hệ thống nhận thức, hệ thống hành động
Mô tả cơ chế hành động xử lý thông tin: Kích thích, vùng đệm, bộ xử lý nhận thức, bộ nhớ ngắn hạn, bộ nhớ dài hạn
GQVĐ là quá trình riêng của xử lý thông tin, đó là cách xuất phát từ 1 tình huống ban đầu nào đó để đi tới đích mong muốn. Tuy nhiên, các phản xạ tức thời, các thao tác đơn thuần thì không được coi là GQVĐ
4 chiến lược GQVĐ của con người:
CL1: Ước lược vấn đề xem xét độ phức tạp.
CL2: Nói lỏng 1 vài ràng buộc.
CL3: Chia bài toán lớn phức tạp thành các bài toán con.
CL4: Tìm cách chuyển các thông tin bên ngoài thành các ký hiệu làm cho bài toán dễ hiểu và dễ giải hơn.
3. Phân loại vấn đề
Định nghĩa: là quá trình xuất phát từ dạng ban đầu và tìm kiếm trong KGBT dãy các phép toán hay các hành động cho phép để đạt được đích mong muốn
Phân loại: 2 loại
Vấn đề phát biểu chỉnh: thỏa mãn 4 điều kiện:  Đích được đặt ra, Biết trạng thái ban đầu,  Xác định được các thao tác,  Có thể nhận biết được 1 lời giải bài toán (đoán hoặc giải)
Vấn đề phát biểu không chỉnh: thỏa mãn 5 điều kiện:  Đích đặt ra không tường minh,  KGBT rời rạc,  KGBT vô hạn,  Các thao tác không được chỉ ra,  Không ràng buộc về mặt thời gian
4. Các thành phần cơ bản của GQVĐ.
GQVĐ là trường hợp riêng của xử lý thông tin, đó là 1 quá trình hành động tư duy gồm 4 thao tác
Thao tác 1: Xác định đích
Thao tác 2: Xác định các sự kiện và các luật có liên quan đến đích
Thao tác 3: Rút gọn để GQVĐ đỡ phức tạp hơn
Thao tác 4: Sử dụng các cơ chế suy diễn phù hợp để đạt được đích mong muốn
GQVĐ là truyền thống
Chương trình = CTDL + GT (truyền thống)
Chương trình = Tri thức + Suy diễn (TTNT)
GQVĐ là các chiến lược điều khiển, tìm kiếm
Xử lý cạnh tranh
Kỹ thuật heuristic: Quay lui, hàm đánh giá
5. Các phương pháp biểu diễn vấn đề: 4pp
Biểu diễn vấn đề bằng KGTT
PP quy bài toán thành các bài toán con
Biểu diễn bằng logic hình thức
Biểu diễn bằng đồ thị
6. GQVĐ bằng tìm kiếm.
Phân loại chiến lược tìm kiếm: 2 loại
Tìm kiếm mù: Không có sự hướng dẫn nào cho việc tìm kiếm,  Phát triển các trạng thái ban đầu cho tới khi gặp một trạng thái đích nào đó. Có 2 kỹ thuật: Tìm kiếm theo chiều rộng và tìm kiếm theo chiều sâu
Tìm kiếm heuristic (kinh nghiệm, mẹo): Sử dụng tri thức đánh giá về các trạng thái để hướng dẫn việc tìm kiếm,  Trong quá trình phát triển các trạng thái, ta chọn trạng thái được đánh giá là tốt nhất để phát triển trong số các trạng thái chờ phát triển -> Gọi là các phương pháp tìm kiếm heuristic.
TK theo chiều rộng: TK tốt nhất-đầu tiên, TT A*
TK theo chiều sâu: Tk leo đồi, TT Nhánh-Cận
Hàm đánh giá và TK heuristic: có 2 chiến lược quan trọng: TK tốt nhất-đầu tiên và Tk leo đồi.
TT A*= Kỹ thuật TK tốt nhất đầu tiên+ Hàm đánh giá


Chương 4:
Mệnh đề (Statement): là phát biểu khẳng định tính ĐÚNG hoặc SAI (True/False)
Câu (Sentence): Câu được cấu tạo từ những ký hiệu sơ cấp theo các luật sau: Tất cả các ký hiệu mệnh đề, ký hiệu chân lý,...đều là câu. Các câu hợp lệ được gọi là các công thức
Biểu thức (Expression): Một biểu thức là một câu hay công thức của phép toán mệnh đề khi và chỉ khi nó được tạo từ những ký hiệu hợp lệ thông qua một dãy các luật
Tri thức: Tri thức được mô tả dưới dạng các câu trong ngôn ngữ biểu diễn tri thức gồm 2 thành phần: Cú pháp và Ngữ nghĩa
- Cú pháp: Các ký hiệu và các quy tắc liên kết các ký hiệu (các luật cú pháp) để tạo thành các câu (công thức) trong ngôn ngữ
- Ngữ nghĩa: Xác định ý nghĩa của các câu của thế giới thực
- Cần cơ chế suy diễn: Ngôn ngữ biểu diễn tri thức cần được cung cấp cơ chế suy diễn. Một luật suy diễn cho phép suy ra một công thức từ một tập các công thức khác
Ngôn ngữ biểu diễn tri thức = Cú pháp + Ngữ nghĩa + Cơ chế suy diễn
Cú pháp: Tập các ký hiệu và tập các luật xây dựng công thức				Ngữ nghĩa: Xác định ý nghĩa của các công thức, ý nghĩa của các phép kết nối logic được biểu diễn qua bảng chân lý
Dạng chuẩn HỘI (CNF - Conjunctive Normal Form) là: Hội của các biểu thức tuyển/literal
Dạng chuẩn TUYỂN (DNF - Disjunctive Normal Form) là: Tuyển của các biểu thức hội/literal
Dạng chuẩn Horn (câu Horn) là: Hội của các biểu thức tuyển, trong đó các biểu thức tuyển có nhiều nhất 1 ký hiệu khẳng định (literal dương)
Các tính chất cơ bản:
A ^ A == A, A v A == A
A ^ 1 == A, A v 1 == A
A ^ 0 == A, A v 0 == 0
A v -A = 1, A ^ -A = 0
A => B


Chương 5:

Biểu diễn tri thức: Là mô tả về thế giới bên ngoài dưới dạng sao cho các máy tính thông minh có thể hiểu được, có thể đưa tới những kết luận về môi trường xung quanh trên cơ sở mô tả các hình thức, các tri thức nhận được.
Dữ liệu: Là các đại lượng mang tính định lượng
Tri thức: Là các đại lượng mang tính định tính. Có thể hiểu tri thức là sự tiến hóa từ dữ liệu, thể hiện:
Chươngtrình=CTDL+Giảithuật
Chươngtrìnhheuristic=Kýhiệutượngtrưng+Giảithuậtheuristic Hệdựatrêntrithức=Trithức+Suydiễn
Các phương pháp biểu diễn
- Biểu diễn bằng logíc hình thức: được thể hiện qua các mệnh đề(pp đc sử dụng phổ biến)
- Biểu diễn bằng hệ sản xuất: gồm các sự kiện, luật Horn(pp đc sử dụng phổ biến)
- Biểu diễn bằng mạng ngữ nghĩa
- Biểu diễn bằng khung tri thức (Frame): biểu diễn tri thức phù hợp với biểu diễn đối tượng, gồm tập hợp các bộ 3 O-A-V
- Biểu diễn bằng bộ 3 tham số O - A – V (Object – Attribute - Value)
Tri thức định lượng: Tri thức mang đặc trưng định tính nhưng liên quan đến các kỹ thuật tính toán, phụ thuộc vào chất lượng của hàm được đánh giá. Hàm đánh giá là cơ sở để chọn chiến lược điều khiển: xử lý cạnh tranh và chọn hướng định tính phù hợp

Tri thức định tính
- Tri thức thủ tục: Đó là phương pháp cấu trúc tri thức, ghép nối và suy diễn các tri thức mới từ các tri thức đã có.
- Tri thức mô tả: Là những thông tin về 1 sự kiện, hiện tượng hay1quá trình mà không đưa ra cấu trúc bên trong, phương pháp sử dụng bên trong. Tri thức mô tả không phụ thuộc vào không gian và thời gian.
- Tri thức điều khiển: Là tri thức điều khiển quá trình xử lý tri thức, nó phối hợp với tri thức thủ tục và tri thức mô tả để thông qua nó điều khiển sự cạnh tranh.
Xử lý tri thức là các kỹ thuật nhằm xây dựng các hệ thống để giải quyết các bài toán có sử dụng tri thức.
Suy diễn là cơ chế liên kết các tri thức đã có để suy ra tri thức mới. Có 2 phương pháp suy diễn:
- Suy diễn tiến (lập luận tiến) (forward chaining): Là quá trình thực hiện 1 chu trình đối sánh – thực thi (match–excecute). Đầu tiên, các sự kiện trong phần vế trái của luật sẽ được kiểm tra, nếu nó thỏa mãn thì luật này khả hợp và thực thi luật này. Quá trình sẽ dừng lại khi tập các sự kiện có chứa phần kết luận.
Ưu điểm
- Làm việc tốt khi bài toán là đi thu thập thông tin rồi thấy điều cần suy diễn.
 - Cho ra khối lượng lớn các thông tin từ một số thông tin ban đầu. Nó sinh ra nhiều thông tin mới
 - Suy diễn tiến là tiếp cận tốt đối với các loại bài toán cần giải quyết các nhiệm vụ như: lập kế hoạch, điều hành, điều khiển và diễn dịch
Nhược điểm
 - Không cảm nhận được rằng chỉ cần một vài thông tin quan trọng. Hệ thống hỏi các câu hỏi có thể hỏi mà không biết rằng chỉ một ít câu đã đi đến kết luận được.
 - Hệ thống có thể hỏi cả câu hỏi không liên quan. Các câu trả lời cũng quan trọng nhưng làm người dùng lúng túng khi trả lời các câu không liên quan đến chủ đề
- Suy diễn lùi (lập luận lùi) (backward chaining): Là quá trình suy diễn xuất phát từ kết luận đã cho đã được chứng minh để tìm ra được các biến phụ cần chứng minh cho đến khi tất cả những gì cần chứng minh đã có trong giả thiết.
Ưu điểm
- Phù hợp với bài toán đưa ra giả thuyết và liệu giả thuyết đó có đúng hay không. - Tập trung vào đích đã cho. Nó tạo ra một loạt câu hỏi chỉ liên quan đến vấn đề đang xét, thuận tiện đối với người dùng
 - Khi suy diễn một điều gì từ thông tin đã biết, nó chỉ tìm trên một phần của cơ sở tri thức thích đáng đối với bài toán đang xét
- Suy diễn lùi được đánh giá cao cho các bài toán: chẩn đoán, dự đoán và tìm lỗi
Nhược điểm: Thường tiếp theo dòng suy diễn thay vì đúng ra phải dừng ở đó mà chuyển sang nhánh khác
CHƯƠNG 6: HỌC MÁY
1. TỔNG QUAN VỀ HỌC MÁY
1.1. Khái niệm cơ bản
Định nghĩa:
Học máy là ngành nghiên cứu thuật toán cho phép máy tính học từ dữ liệu
Học máy cải thiện hiệu quả công việc thông qua kinh nghiệm
Biểu diễn bài toán: (T, P, E)
T (Task): Nhiệm vụ cần thực hiện
P (Performance): Tiêu chí đánh giá hiệu năng
E (Experience): Kinh nghiệm từ dữ liệu
Ví dụ minh họa:
Bài toán: Lọc thư rác
T: Phân loại email là rác hay không rác
P: Tỷ lệ % email được phân loại đúng
E: Tập các email đã được gán nhãn
1.2. Phân loại học máy
A. Học có giám sát (Supervised Learning)
Dữ liệu có cả đầu vào và đầu ra
Phân loại: Đầu ra rời rạc (VD: rác/không rác)
Hồi quy: Đầu ra liên tục (VD: dự đoán giá nhà)
B. Học không giám sát (Unsupervised Learning)
Dữ liệu chỉ có đầu vào
Phân cụm: Nhóm dữ liệu tương tự (VD: phân nhóm khách hàng)
Luật kết hợp: Tìm mối quan hệ (VD: khách mua A thường mua B)
C. Học bán giám sát (Semi-supervised)
Một phần dữ liệu có nhãn, phần còn lại không
D. Học tăng cường (Reinforcement Learning)
Học từ phần thưởng/phạt của môi trường
1.3. Chia tập dữ liệu
Tổng dữ liệu 100%
├── Training set (60-80%): Huấn luyện mô hình
├── Validation set (10-20%): Tối ưu tham số
└── Test set (10-20%): Đánh giá cuối cùng
1.4. Vấn đề quan trọng
Overfitting (Quá khớp)
Mô hình học quá tốt trên tập huấn luyện
Kém hiệu quả trên dữ liệu mới
Nguyên nhân: Mô hình quá phức tạp, dữ liệu ít, nhiễu
Underfitting (Kém khớp)
Mô hình quá đơn giản
Không nắm bắt được xu hướng dữ liệu
Định lý No-free-lunch
Không có thuật toán nào tốt nhất cho MỌI bài toán
Cần chọn thuật toán phù hợp với từng miền ứng dụng
2. MẠNG NƠ RON NHÂN TẠO (ANN)
2.1. Mô hình nơ ron cơ bản
Công thức:
Net = Σ(wⱼ × sⱼ) - θ
out = g(Net)
Trong đó:
wⱼ: trọng số liên kết
sⱼ: tín hiệu vào
θ: ngưỡng
g: hàm kích hoạt
3 hàm kích hoạt phổ biến:
Hàm dấu (Sign)
g(x) = { 1 nếu x ≥ 0
   	{-1 nếu x < 0
Hàm Sigmoid
g(x) = 1/(1 + e^(-x))
Giá trị: (0, 1)
Hàm tuyến tính từng đoạn
g(x) = { 1 nếu x ≥ θ₁
   	{ x nếu θ₂ < x < θ₁
   	{ 0 nếu x ≤ θ₂
2.2. Mạng Perceptron (1 lớp)
Thuật toán học:
1. Khởi tạo trọng số ngẫu nhiên [-0.5, 0.5]
2. Với mỗi mẫu (Xₛ, Yₛ):
   - Tính out = g(Σwⱼ×xⱼ)
   - Err = Yₛ - out
   - Cập nhật: wⱼ = wⱼ + η×xⱼ×Err
3. Lặp đến khi hội tụ
Khả năng:
Có thể biểu diễn: AND, OR, NOT
Không thể biểu diễn: XOR (cần nhiều lớp)
2.3. Mạng Hopfield
Đặc điểm:
Mạng 1 lớp, liên kết đầy đủ
Tự kết hợp (auto-association)
Ứng dụng: Phục hồi mẫu có nhiễu
Công thức trọng số:
wⱼᵢ = Σ(xₛᵢ × xₛⱼ) với s = 1→p
(p là số mẫu học)

Điều kiện: wᵢᵢ = 0 (không tự liên kết)
Quá trình sử dụng:
1. X(0) = X_input
2. Lặp:
   Y(t) = sign(W × X(t))
   Nếu Y(t) = X(t) → Dừng
   Ngược lại: X(t+1) = Y(t)
2.4. Mạng lan truyền ngược (Backpropagation)
Cấu trúc:
Nhiều lớp ẩn
Lan truyền tiến (Forward) + Lan truyền ngược (Backward)
Thuật toán:
Bước 1: Forward (Lan truyền tiến)
Với mỗi lớp từ input → output:
  Netᵢ = Σ(wᵢⱼ × aⱼ)
  aᵢ = g(Netᵢ)
Bước 2: Backward (Lan truyền ngược)
Lớp ra:
δᵢ = Errᵢ × g'(Netᵢ)
wᵢⱼ = wᵢⱼ + η × aⱼ × δᵢ
Lớp ẩn:
δⱼ = g'(Netⱼ) × Σ(wᵢⱼ × δᵢ)
wⱼₖ = wⱼₖ + η × aₖ × δⱼ
Khả năng:
1 lớp ẩn: Xấp xỉ hàm liên tục
2 lớp ẩn: Xấp xỉ hàm bất kỳ
3. LOGIC MỜ (FUZZY LOGIC)
3.1. Tập mờ cơ bản
Định nghĩa:
Tập mờ Ā trên U có hàm thuộc: μ_Ā: U → [0,1]
μ_Ā(x) = độ thuộc của x vào Ā
Biểu diễn:
U đếm được:
Ā = μ₁/x₁ + μ₂/x₂ + ... + μₙ/xₙ
Ví dụ:
U = {20, 30, 40, 50, 60} (tuổi)
Ā_trẻ = 1.0/20 + 0.8/30 + 0.5/40 + 0.2/50 + 0.0/60
3.2. Các phép toán tập mờ
1. Phép HỢP (∪)
μ_(Ā∪B̄)(x) = max{μ_Ā(x), μ_B̄(x)}
2. Phép GIAO (∩)
μ_(Ā∩B̄)(x) = min{μ_Ā(x), μ_B̄(x)}
3. Phần BÙ (¬)
μ_Ā̄(x) = 1 - μ_Ā(x)
4. Tổng đại số (⊕)
μ_(Ā⊕B̄)(x) = μ_Ā(x) + μ_B̄(x) - μ_Ā(x)×μ_B̄(x)
5. Tích đại số (⊗)
μ_(Ā⊗B̄)(x) = μ_Ā(x) × μ_B̄(x)
3.3. Tập mức và tập rõ
Tập mức α (α-cut)
Ā_α = {x ∈ U | μ_Ā(x) ≥ α}
Tập rõ gần nhất
μ_Â(x) = { 1 nếu μ_Ā(x) ≥ 0.5
     	{ 0 nếu μ_Ā(x) < 0.5
3.4. Khoảng cách và chỉ số mờ
Khoảng cách Hamming
d(Ā,B̄) = Σ|μ_Ā(xᵢ) - μ_B̄(xᵢ)|
Khoảng cách Hamming tương đối
ρ(Ā,B̄) = d(Ā,B̄)/m
(m = số phần tử)
Khoảng cách Euclid
e(Ā,B̄) = √[Σ(μ_Ā(xᵢ) - μ_B̄(xᵢ))²]
Chỉ số mờ theo Hamming
ℑ(Ā) = 2×d(Ā,Â)/n
Chỉ số mờ theo Euclid
ℑ(Ā) = 2×e(Ā,Â)/√n
 VÍ DỤ VỀ MẠNG NƠ RON NHÂN TẠO
Ví dụ 2: Mạng Perceptron - Cổng logic AND
Bài toán: Xây dựng mạng Perceptron để mô phỏng cổng AND
Dữ liệu huấn luyện:
x₁
x₂
y (mục tiêu)
000
010
100
111

Quá trình huấn luyện:
Bước 1: Khởi tạo trọng số ngẫu nhiên
w₁ = 0.3, w₂ = 0.3, θ = -0.5
Hệ số học: η = 0.1
Bước 2: Huấn luyện với mẫu (0,0) → y = 0
- Net = w₁*0 + w₂*0 - θ = 0 - (-0.5) = 0.5
- out = sign(0.5) = 1
- Err = 0 - 1 = -1
- Cập nhật:
  w₁ = 0.3 + 0.1*0*(-1) = 0.3
  w₂ = 0.3 + 0.1*0*(-1) = 0.3
  θ = -0.5 + 0.1*(-1)*(-1) = -0.4
Bước 3: Huấn luyện với mẫu (0,1) → y = 0
- Net = 0.3*0 + 0.3*1 - (-0.4) = 0.7
- out = sign(0.7) = 1
- Err = 0 - 1 = -1
- Cập nhật:
  w₁ = 0.3
  w₂ = 0.3 + 0.1*1*(-1) = 0.2
  θ = -0.4 + 0.1*(-1) = -0.5
... (tiếp tục cho đến khi hội tụ)
Kết quả cuối: w₁ = 0.5, w₂ = 0.5, θ = -0.7
Ví dụ 3: Mạng Hopfield - Nhớ và phục hồi mẫu
Bài toán: Lưu trữ 2 mẫu và phục hồi khi có nhiễu
Dữ liệu:
Mẫu 1: X¹ = [1, -1, 1]	(mẫu "A")
Mẫu 2: X² = [-1, 1, -1]   (mẫu "B")
Bước 1: Tính ma trận trọng số W
w₁₁ = x¹₁*x¹₁ + x²₁*x²₁ = 1*1 + (-1)*(-1) = 2
w₁₂ = x¹₁*x¹₂ + x²₁*x²₂ = 1*(-1) + (-1)*1 = -2
w₁₃ = x¹₁*x¹₃ + x²₁*x²₃ = 1*1 + (-1)*(-1) = 2
w₂₂ = x¹₂*x¹₂ + x²₂*x²₂ = (-1)*(-1) + 1*1 = 2
w₂₃ = x¹₂*x¹₃ + x²₂*x²₃ = (-1)*1 + 1*(-1) = -2
w₃₃ = x¹₃*x¹₃ + x²₃*x²₃ = 1*1 + (-1)*(-1) = 2
Ma trận W:
	[ 2  -2   2 ]
W = [-2   2  -2 ]
	[ 2  -2   2 ]
Bước 2: Phục hồi mẫu có nhiễu
Input: X = [1, 1, 1] (mẫu "A" bị nhiễu)
Lần 1:
- Net₁ = 2*1 + (-2)*1 + 2*1 = 2 → out₁ = 1
- Net₂ = (-2)*1 + 2*1 + (-2)*1 = -2 → out₂ = -1
- Net₃ = 2*1 + (-2)*1 + 2*1 = 2 → out₃ = 1
- Y(1) = [1, -1, 1]
Lần 2:
- Input X(2) = [1, -1, 1]
- Tính lại → Y(2) = [1, -1, 1]
- Y(2) = X(2) → Dừng
Kết quả: Phục hồi được mẫu "A" = [1, -1, 1]
Ví dụ 4: Mạng lan truyền ngược (Backpropagation)
Bài toán: Học hàm XOR
Cấu trúc mạng:
Input layer: 2 nơ ron (x₁, x₂)
Hidden layer: 2 nơ ron (h₁, h₂)
Output layer: 1 nơ ron (y)
Dữ liệu huấn luyện:
x₁
x₂
y
000
011
101
110

Quá trình huấn luyện với mẫu (1,0) → y = 1:
Giả sử trọng số ban đầu:
w₁₁ = 0.5, w₁₂ = -0.3 (từ x₁, x₂ đến h₁)
w₂₁ = 0.2, w₂₂ = 0.4  (từ x₁, x₂ đến h₂)
v₁ = 0.6, v₂ = -0.5   (từ h₁, h₂ đến y)
η = 0.5 (hệ số học)
Hàm kích hoạt: sigmoid σ(x) = 1/(1+e⁻ˣ)
Bước 1: Lan truyền tiến (Forward)
- Lớp ẩn:
  Net_h₁ = 0.5*1 + (-0.3)*0 = 0.5
  a_h₁ = σ(0.5) = 0.622
  Net_h₂ = 0.2*1 + 0.4*0 = 0.2
  a_h₂ = σ(0.2) = 0.550
- Lớp ra:
  Net_y = 0.6*0.622 + (-0.5)*0.550 = 0.098
  out = σ(0.098) = 0.524
Bước 2: Tính sai số
- Err = 1 - 0.524 = 0.476
Bước 3: Lan truyền ngược (Backward)
- Lớp ra:
  δ_y = Err * σ'(Net_y) = 0.476 * 0.524 * (1-0.524) = 0.119
  Cập nhật trọng số:
  v₁ = 0.6 + 0.5*0.622*0.119 = 0.637
  v₂ = -0.5 + 0.5*0.550*0.119 = -0.467
- Lớp ẩn:
  δ_h₁ = σ'(Net_h₁) * v₁ * δ_y = 0.622*(1-0.622) * 0.6 * 0.119 = 0.017
  δ_h₂ = σ'(Net_h₂) * v₂ * δ_y = 0.550*(1-0.550) * (-0.5) * 0.119 = -0.015

  Cập nhật trọng số:
  w₁₁ = 0.5 + 0.5*1*0.017 = 0.509
  w₁₂ = -0.3 + 0.5*0*0.017 = -0.3
  w₂₁ = 0.2 + 0.5*1*(-0.015) = 0.193
  w₂₂ = 0.4 + 0.5*0*(-0.015) = 0.4

3. VÍ DỤ VỀ LOGIC MỜ
Ví dụ 5: Tập mờ "Người trẻ"
Cho: U = {10, 20, 30, 40, 50, 60} (tuổi)
Định nghĩa tập mờ "Trẻ":
Ā_trẻ = 1.0/10 + 0.9/20 + 0.6/30 + 0.3/40 + 0.1/50 + 0.0/60
Hay viết: Ā_trẻ = {(10, 1.0), (20, 0.9), (30, 0.6), (40, 0.3), (50, 0.1), (60, 0.0)}
Các phép toán:
a) Tập mức α-cut:
α = 0.3: Ā₀.₃ = {10, 20, 30, 40}
α = 0.5: Ā₀.₅ = {10, 20, 30}
α = 0.9: Ā₀.₉ = {10, 20}
b) Tập rõ gần nhất:
Â = {10, 20, 30} (các phần tử có μ ≥ 0.5)
Ví dụ 6: Tính chỉ số mờ
Cho tập mờ:
A = 0.3/x₁ + 0.9/x₂ + 0.7/x₃ + 0.4/x₄
Bước 1: Xác định tập rõ gần nhất
Với ngưỡng 0.5:
- μ_A(x₁) = 0.3 < 0.5 → μ_Â(x₁) = 0
- μ_A(x₂) = 0.9 ≥ 0.5 → μ_Â(x₂) = 1
- μ_A(x₃) = 0.7 ≥ 0.5 → μ_Â(x₃) = 1
- μ_A(x₄) = 0.4 < 0.5 → μ_Â(x₄) = 0
Â = 0/x₁ + 1/x₂ + 1/x₃ + 0/x₄
Bước 2: Tính chỉ số mờ theo Hamming
d(A,Â) = |0.3-0| + |0.9-1| + |0.7-1| + |0.4-0| = 0.3 + 0.1 + 0.3 + 0.4 = 1.1

ℑ(A) = 2*d(A,Â)/n = 2*1.1/4 = 0.55
Bước 3: Tính chỉ số mờ theo Euclid
e(A,Â) = √[(0.3-0)² + (0.9-1)² + (0.7-1)² + (0.4-0)²]= √[0.09 + 0.01 + 0.09 + 0.16]= √0.35
ℑ(A) = 2*e(A,Â)/√n = 2*0.592/√4 = 2*0.592/2 = 0.592
Ví dụ 7: Phép hợp và giao tập mờ
Cho 2 tập mờ:
A = 0.7/x₁ + 0.4/x₂ + 0.9/x₃
B = 0.5/x₁ + 0.8/x₂ + 0.3/x₃
a) Phép HỢP (Union):
μ_(A∪B)(xᵢ) = max{μ_A(xᵢ), μ_B(xᵢ)}
A∪B = max(0.7,0.5)/x₁ + max(0.4,0.8)/x₂ + max(0.9,0.3)/x₃ = 0.7/x₁ + 0.8/x₂ + 0.9/x₃
b) Phép GIAO (Intersection):
μ_(A∩B)(xᵢ) = min{μ_A(xᵢ), μ_B(xᵢ)}
A∩B = min(0.7,0.5)/x₁ + min(0.4,0.8)/x₂ + min(0.9,0.3)/x₃ = 0.5/x₁ + 0.4/x₂ + 0.3/x₃
c) Phần BÙ:
μ_Ā(xᵢ) = 1 - μ_A(xᵢ)
Ā = (1-0.7)/x₁ + (1-0.4)/x₂ + (1-0.9)/x₃ = 0.3/x₁ + 0.6/x₂ + 0.1/x₃
d) Tổng đại số:
μ_(A⊕B)(xᵢ) = μ_A(xᵢ) + μ_B(xᵢ) - μ_A(xᵢ)*μ_B(xᵢ)
A⊕B = [0.7+0.5-0.7*0.5]/x₁ + [0.4+0.8-0.4*0.8]/x₂ + [0.9+0.3-0.9*0.3]/x₃ = 0.85/x₁ + 0.88/x₂ + 0.93/x₃
e) Tích đại số:
μ_(A⊗B)(xᵢ) = μ_A(xᵢ) * μ_B(xᵢ)
A⊗B = (0.7*0.5)/x₁ + (0.4*0.8)/x₂ + (0.9*0.3)/x₃= 0.35/x₁ + 0.32/x₂ + 0.27/x₃
Ví dụ 8: Phân tích tập mờ qua tập rõ (theo slide BTVD 2)
Cho:
U = {x₁, x₂, x₃, x₄, x₅, x₆, x₇}
Các tập mức:
A₀.₃ = {x₃, x₄, x₅, x₆, x₇}
A₀.₅ = {x₃, x₄, x₅, x₆, x₇}
A₀.₇ = {x₃, x₅, x₆}
A₀.₉ = {x₅, x₆}
Phân tích ngược lại các giá trị độ thuộc:
Từ các tập mức, suy ra:
- x₁: không thuộc tập nào → μ_A(x₁) = 0.1
- x₂: không thuộc tập nào → μ_A(x₂) = 0 (giả sử)
- x₃: thuộc A₀.₃, A₀.₅ nhưng không thuộc A₀.₇ → μ_A(x₃) = 0.5
- x₄: thuộc A₀.₃, A₀.₅ nhưng không thuộc A₀.₇ → μ_A(x₄) = 0.6
- x₅: thuộc tất cả kể cả A₀.₉ → μ_A(x₅) = 0.9
- x₆: thuộc tất cả kể cả A₀.₉ → μ_A(x₆) = 1.0
- x₇: thuộc A₀.₃, A₀.₅ nhưng không thuộc A₀.₇ → μ_A(x₇) = 0.5
Công thức phân tích:
A = 0.1·{x₁,x₃,x₄,x₅,x₆,x₇} ∪ 0.5·{x₃,x₄,x₅,x₆,x₇} ∪ 0.6·{x₃,x₄,x₅,x₆} ∪ 0.7·{x₃,x₅,x₆} ∪ 0.9·{x₅,x₆} ∪ 1.0·{x₆}

TRẮC NGHIỆM
Có bn quy tắc trong giải thuật TK theo chiều rộng =>  qui tắc
Giải thuật TK theo CR bắt đầu duyệt từ => Nút gốc
“Nếu k tìm thấy đỉnh liền kề, thì xoá đỉnh đầu tiên trong hàng đợi” là quy tắc thứ mấy trong TK theo CR => Qui tắc thứ 2
Đâu k phải là ứng dụng của giải thuật TK theo CR trong bài toán lý thuyết đồ thị => TK có giới hạn
=> Ứng dụng: Tìm đường đi ngắn nhất, Tìm các thành phần liên thông, Tìm tất cả các đỉnh trong 1 thành phần liên thông.
Nếu số đỉnh là hữu hạn thì giải thuật TK theo CR có tìm ra kq không? => Có
Giải thuật TK theo CR có bn tính chất => 2 tính chất
Giải thuật TK theo CR có tính chất vét cạn, vậy có nên áp dụng vào đồ thị có số đỉnh lớn không? => Không nên
GT TK theo CR => Duyệt tất cả các đỉnh
GT TK theo CR => Sử dụng ngăn xếp
Có bn qui tắc trong GT TK theo chiều sâu => 3 quy tắc
TK theo CS có giới hạn là gì => Là 1 TT phát triển các nút chưa xét các theo chiều sâu nhưng có giới hạn mức
GT TK theo CS dần có sd KGTT O(bxL) không => Có sd
TK theo giá thành thống nhất là tối ưu vì => Con đường có chi phí thấp nhất đc chọn
TT nào đc đưa ra để khắc phục điểm yếu của TT TK giới hạn độ sâu DLS => TK sâu dần
GTTK sâu dần thường áp dụng cho bài toán nào => Btoan có KGTT lớn và độ sâ của nghiệm là k biết trc
Trong GT TK leo đồi => Khi phát triển 1 đỉnh u thì bước tiếp theo ta chọn trong số các đỉnh con của u, đỉnh nào có nhiều hứa hẹn nhất để phát triển, đỉnh này đc xđ = hàm đánh giá
GT TK nhánh cận giải quyết các bài toán nào => Các btoan tối ưu tổ hợp
GT nhánh cận là 1 dạng tiến của TT nào => GT quay lui
Ưu điểm GT nhánh cận => Không quét qua toàn bộ nghiệm có thể có của btoan
Có mấy GT dựa vào GTTK tốt nhất đầu tiên => 3 giải thuật( A*)
GTTK tốt nhất đầu tiên kết hợp 2 ưu điểm của 2 GT nào => GT TK theo CR và GT TK theo CS
Đáp án đúng nói về GTTK tốt nhất đầu tiền => có thể bị kẹt trọng 1 vòng lặp như DFS
GT A* được công bố lần đầu vào => 1986
GT A*=> Tốn khá nhiều bộ nhớ để lưu lại những trạng thái đã đi qua
Thông tin luật đánh giá heuristic về bài toán đc biểu diễn bằng luật điều khiển dưới dạng => If then
SD thuật giải Heuristic => Nhanh chóng và dễ dàng đưa ra kq do vậy chi phí thấp
GT heuristic thường thể hiện => Khá tự nhiên, gần gũi với cách suy nghĩ và hành động của con người
GT đồ thị và hoặc => GT sd chỉ 1 hàm ước lượng Heuristic để đánh giá 1 trạng thái trong đồ thị
GT đồ thị và hoặc => SD 1 danh sách S nhằm mục đích cho quá trình truyền lùi về gốc của đồ thị
Đâu k là đặc trưng của hệ chuyên gia => Kh sd thông tin Heuristic
( Đặc trưng: Sd tri thức chuyên gia, sd kĩ thuật tìm kiếm, có khả năng xử lí kí hiệu)
Toán học logic xuất phát điểm từ => Tập hợp các câu đơn giản ghi nhận lại các sự kiện đã xảy ra trong 1 không gian và thời gian xác định nào đó
Có mấy loại toán học logic => 2 loại


