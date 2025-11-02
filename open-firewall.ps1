# PowerShell script to open firewall port 8000
# Run this as Administrator: Right-click > Run as Administrator

Write-Host "Opening Windows Firewall for Python Server..." -ForegroundColor Green

# Add firewall rule
$rule = @{
    DisplayName = "Python Server Port 8000"
    Direction = "Inbound"
    LocalPort = 8000
    Protocol = "TCP"
    Action = "Allow"
    Enabled = "True"
}

try {
    New-NetFirewallRule -DisplayName $rule.DisplayName `
                        -Direction $rule.Direction `
                        -LocalPort $rule.LocalPort `
                        -Protocol $rule.Protocol `
                        -Action $rule.Action `
                        -Enabled $rule.Enabled `
                        -ErrorAction Stop
    
    Write-Host "[OK] Firewall rule added successfully!" -ForegroundColor Green
    Write-Host "[*] Port 8000 is now open for incoming connections" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Now you can access the server from other devices on the same network." -ForegroundColor Cyan
} catch {
    if ($_.Exception.Message -like "*already exists*") {
        Write-Host "[INFO] Firewall rule already exists" -ForegroundColor Yellow
    } else {
        Write-Host "[ERROR] Failed to add firewall rule: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "[TIP] Make sure you're running PowerShell as Administrator" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

