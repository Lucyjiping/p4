echo "		Testing Report with Mixed Samll Packets " | tee report.docx

echo "Data file name: h2_50_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_50_mix_tos.log | tee -a report.docx

echo "Data file name: h2_100_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_100_mix_tos.log | tee -a report.docx


echo "Data file name: h2_200_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_200_mix_tos.log | tee -a report.docx

echo "Data file name: h2_300_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_300_mix_tos.log | tee -a report.docx

echo "Data file name: h2_500_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_500_mix_tos.log | tee -a report.docx

echo "Data file name: h2_1000_mix_tos.log " |tee -a report.docx
./classify_pkt.py h2_1000_mix_tos.log | tee -a report.docx




echo "Data file name: h2_50_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_50_mix_1_tos.log | tee -a report.docx

echo "Data file name: h2_100_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_100_mix_1_tos.log | tee -a report.docx


echo "Data file name: h2_200_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_200_mix_1_tos.log | tee -a report.docx

echo "Data file name: h2_300_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_300_mix_1_tos.log | tee -a report.docx

echo "Data file name: h2_500_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_500_mix_1_tos.log | tee -a report.docx

echo "Data file name: h2_1000_mix_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_1000_mix_1_tos.log | tee -a report.docx


