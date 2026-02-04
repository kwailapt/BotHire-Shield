const fs = require('fs');
const report = JSON.parse(fs.readFileSync('malfunction_report.json'));

if (report.status === "MALICIOUS_ACTIVITY_DETECTED") {
    console.error("🚨 [Protocol Breach] Malicious payload detected in report!");
    process.exit(1); // 強制測試失敗，觸發 GitHub Actions
}
