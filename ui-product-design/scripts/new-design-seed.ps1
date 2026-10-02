[CmdletBinding()]
param(
    [ValidateRange(32, 512)]
    [int]$Length = 128
)

$ErrorActionPreference = 'Stop'
$alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
$buffer = New-Object byte[] 256
$builder = [System.Text.StringBuilder]::new($Length)
$generator = [System.Security.Cryptography.RandomNumberGenerator]::Create()

try {
    while ($builder.Length -lt $Length) {
        $generator.GetBytes($buffer)
        foreach ($value in $buffer) {
            # 248 is divisible by 62: rejection avoids modulo bias.
            if ($value -lt 248) {
                [void]$builder.Append($alphabet[$value % $alphabet.Length])
                if ($builder.Length -eq $Length) { break }
            }
        }
    }
    $builder.ToString()
}
finally {
    $generator.Dispose()
}
