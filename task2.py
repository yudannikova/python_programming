min_in = int(input())
H_in = int(input())
M_in = int(input())
min_total = min_in+H_in*60+M_in
h_out = min_total//60
m_out = min_total-h_out*60
print (h_out)
print (m_out)