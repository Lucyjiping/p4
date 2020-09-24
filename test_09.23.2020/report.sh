echo "		Testing Report without Mixed Packets " | tee report.docx

echo "Data file name: h2_100_tos.log " |tee -a report.docx
./classify_pkt.py h2_100_tos.log | tee -a report.docx

echo "Data file name: h2_200_tos.log " |tee -a report.docx
./classify_pkt.py h2_200_tos.log | tee -a report.docx


echo "Data file name: h2_300_1_tos.log " |tee -a report.docx
./classify_pkt.py h2_300_1_tos.log | tee -a report.docx

echo "Data file name: h2_400_tos.log " |tee -a report.docx
./classify_pkt.py h2_400_tos.log | tee -a report.docx

echo "Data file name: h2_500_tos.log " |tee -a report.docx
./classify_pkt.py h2_500_tos.log | tee -a report.docx

echo "Data file name: h2_1000_tos.log " |tee -a report.docx
./classify_pkt.py h2_1000_tos.log | tee -a report.docx

