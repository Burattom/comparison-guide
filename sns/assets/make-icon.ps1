Add-Type -AssemblyName System.Drawing

$bmp = New-Object System.Drawing.Bitmap 500,500
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::FromArgb(255,250,247,242))
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias

$red      = [System.Drawing.Color]::FromArgb(255,178,58,46)
$darkRed  = [System.Drawing.Color]::FromArgb(255,120,36,30)
$gold     = [System.Drawing.Color]::FromArgb(255,201,162,39)
$cream    = [System.Drawing.Color]::FromArgb(255,255,246,232)

# outer ring
$pen = New-Object System.Drawing.Pen($red, 16)
$g.DrawEllipse($pen, 28, 28, 444, 444)

# lid
$g.FillRectangle((New-Object System.Drawing.SolidBrush($darkRed)), 110, 96, 280, 34)
$g.FillEllipse((New-Object System.Drawing.SolidBrush($darkRed)), 235, 80, 30, 22)

# tier 1 (top)
$g.FillRectangle((New-Object System.Drawing.SolidBrush($red)), 120, 142, 260, 66)
# tier 2 (middle)
$g.FillRectangle((New-Object System.Drawing.SolidBrush($gold)), 108, 220, 284, 66)
# tier 3 (bottom)
$g.FillRectangle((New-Object System.Drawing.SolidBrush($red)), 120, 298, 260, 66)

# simple food dots on each tier
$brushCream = New-Object System.Drawing.SolidBrush($cream)
foreach ($y in 158, 236, 314) {
  $g.FillEllipse($brushCream, 150, $y, 22, 22)
  $g.FillEllipse($brushCream, 200, $y, 22, 22)
  $g.FillEllipse($brushCream, 250, $y, 22, 22)
  $g.FillEllipse($brushCream, 300, $y, 22, 22)
}

# base
$g.FillRectangle((New-Object System.Drawing.SolidBrush($darkRed)), 96, 372, 308, 20)

$g.Dispose()
$bmp.Save('D:\ssdproject\A8-afiliate\sns\assets\profile-icon.png', [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Output 'created'
