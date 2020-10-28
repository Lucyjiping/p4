echo "		Audio Test Report without Mixed Packets " | tee report.docx

echo "Data file name: h2_audio_100_tos.log " |tee -a report.docx
./classify_pkt.py h2_audio_100_tos.log | tee -a report.docx

echo "Data file name: h2_audio_300_tos.log " |tee -a report.docx
./classify_pkt.py h2_audio_300_tos.log | tee -a report.docx


echo "Data file name: h2_audio_500_tos.log " |tee -a report.docx
./classify_pkt.py h2_audio_500_tos.log | tee -a report.docx

echo "Data file name: h2_audio_700_tos.log " |tee -a report.docx
./classify_pkt.py h2_audio_700_tos.log | tee -a report.docx


