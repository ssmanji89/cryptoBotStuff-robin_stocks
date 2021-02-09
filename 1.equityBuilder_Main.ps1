function startEquityBots() {
    <#
        NOTES: 
            - LAST 500 TWEETS FROM @unusual_whales
            - LOOSE ON RESTRICTIONS
            -- ( ($relVolume -gt 0 -and $relVolume -lt 2) -and $rsi -lt 60 -and $change -lt 3 -and $weekPerf -lt 5)
            - RHBOT IS SET TO low() [PASSIVELY BUY AND HOLD]
            -  
    #>

    $sleepSeconds = 0.00; 

    $env:AccessTokenSecret = "rp5FHnWKR8NwboCbf4wkuAIXpKHJhquK2a4u0uR657a5s"
    $env:APISecret = "lKpLEvkO3Jyltw0C8e8j5RSeK3GPGbTgBaQCMgKyOuPkSk5RFh"
    $env:AccessToken = "186253946-54beRf0jjRl2F3SU4LnWl8Mg6yvtNPOX5JfT1buz"
    $env:APIKey="DT4d5n6um9xf3P3ap2L19N7pZ";

    $OAuthSettings = @{
        ApiKey = $env:ApiKey
        ApiSecret = $env:ApiSecret
        AccessToken = $env:AccessToken
        AccessTokenSecret =$env:AccessTokenSecret
    }
    Set-TwitterOAuthSettings @OAuthSettings -ErrorAction SilentlyContinue; 


    $outputFilename = ('Squeeeze_Stalking_'+(Get-Date -Format 'dd-H')+'_sullyStocks-AIO.py');
    $mainOutputFile = ('D:\Scripts\!PowerShell\!Financial\Squeeeze_Stalking_'+(Get-Date -Format 'dd-H')+'_sullyStocks-AIO.py'); 

    '#Start OpenInsider_Stalking_RISK_' | Out-File ("D:\!DUMP\allBuys_OnlySympbols_"+(Get-Date -Format 'MM.dd.y')+".txt") -Append;
    ('#>'+$mainOutputFile) | Out-File ("D:\!DUMP\allBuys_OnlySympbols_"+(Get-Date -Format 'MM.dd.y')+".txt") -Append;
    Remove-Item ("D:\!DUMP\"+$outputFilename) -Force;
    Remove-Item $mainOutputFile -Force;
        

    cls;
    cd ('D:\Scripts\!PowerShell\robin_stocks-master')

    $newBuys = ''
    $todaysBuys = ''
    $dataFromStockTwits = ''
    $dataFromCSV = ''; 
    $dataAsCSV = ''; 

    $totalPositionSize = 0.00;
    $OFS = "`r`n"
    $ErrorActionPreference = 'SilentlyContinue'    
    $finallyTweetSymbols = @{};
    $tweetSymbolString = '';
    $finalTweetSymbols = '';
    $tweets = '';
    $tweetSymbols = ''; 
    $tweetsFiltered = ''; 
    $twets = $OFS; 
    $twits = '';
    $tempTwits = '';
    $finTweets = '';
    $finnSyms = '';
    $finSyms = '';
    $dataFromStockTwits = ''; 
    $syms = ''; 
    $dataFromCSV =''; $dataFromCSV1 =''; $dataFromStockTwits = ''; $tweets = '';
    $watchHumans = ('unusual_whales');    

    foreach ($h in $watchHumans) {
    $tweets = Get-TwitterStatuses_UserTimeline -screen_name $h -count 1000 | Where-Object {$_ -match '\$\w+\ \d+\-\d+\-\d+\ C'} | select -ExpandProperty text;
    #$allTweets = $allTweets + $tweets + ', '
        foreach ($g in $tweets) {
            foreach ($l in $g.split(' ')[0]) {
                foreach ($k in $l.split(' ')[0]) {
                    $dataFromCSV1 = ($dataFromCSV1+','+(($k.Replace('.','')).replace('$','')).toUpper())
    }}}}

    foreach ($r in ($dataFromCSV1.Split(','))) {
        $dataFromCSV = ($dataFromCSV+$r+',')   
    }

    $syms = ($syms + $dataFromCSV)
    $dataFromStockTwits = (($dataFromCSV).Split(',') | Group-Object | select -ExpandProperty name);
    $discordWebhook = ''
    $discordWebhook = 'https://discordapp.com/api/webhooks/767568117823963146/fd5NRKbydSBz4J_1io7duVxOeymGYbfQUDUGPWWuYsZftooPUa21-SwpXETxioNcEppm'; 
    $discordName = 'PS#AIO'
    $finvizURLS = ''
    $finvizURLSProcd = '';

    foreach ($i in ($dataFromStockTwits | Group-Object | select -ExpandProperty name)) {
            $symbol = $i

            $symbolFinViz = ('https://finviz.com/quote.ashx?t='+$symbol+', ');

            $finvizURLS = $finvizURLS + $symbolFinViz
    }
    $finvizURLSProcd = $finvizURLS

    #initiate py script
    $rValueUpper = 40; 
    $rValueLower = 25; 

    #Analyst Actions
    $timeinforce = ('gfd');
    $priceType = ('ask_price');
    $cnt=0; 
    $change = ''; 
    $searchClass = "snapshot-td2" 
    $myURI = ($curSym) 
    
    ("#>Total Symbols being Evaluated: " + ($dataFromStockTwits.Count)) | Out-File ($mainOutputFile) -Append;

    ("#>>List: " + $dataFromCSV) | Out-File ($mainOutputFile) -Append;

    $OFS | Out-File ($mainOutputFile) -Append;
    "import os "+$OFS | Out-File ($mainOutputFile) -Append
    "import time "+$OFS | Out-File ($mainOutputFile) -Append
    "import sys "+$OFS | Out-File ($mainOutputFile)  -Append
    "import robin_stocks as rs"+$OFS | Out-File ($mainOutputFile)  -Append
    ("rs.login(username="+"'"+$ruser+"'"+", password=("+"'"+$rpass+"'"+"), expiresIn=86400, by_sms=True)") | Out-File ($mainOutputFile) -Append;
        
    $insTrans = 0.00; 
    $instTrans = 0.00; 
    $rsi = 0.00; 

    $discordWebhook = ''
    $discordWebhook = 'https://discordapp.com/api/webhooks/767568117823963146/fd5NRKbydSBz4J_1io7duVxOeymGYbfQUDUGPWWuYsZftooPUa21-SwpXETxioNcEppm'; 
    $discordName = 'PS#AIO'

    foreach ($h in $finvizURLSProcd.split(',')) {
        $curSym = '';
	    $rsi = 0.00;$all = 0.00;$price = 0.00;$change = 0.00;$weekPerf = 0.00;$relVolume = 0.00;$insTrans = 0.00;$instTrans = 0.00;$institutionOwnership = 0.00;$insiderOwnership = 0.00;
        $cnt = $cnt+1; 
    IF ($h -notlike '*=') {
    $curSym = $h; 
    ('#Start '+((($curSym.Split('=')[1]).trim()).REPLACE(' ', ''))+$OFS) | Out-File ($mainOutputFile) -Append;
    $myURI = ($curSym) 
    #("#"+$myURI) | Out-File ("D:\!DUMP\"+$outputFilename) -Append
    $fullall = ''; $upgradesall = ''; 
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 <# using TLS 1.2 is vitally important #>
    $req = Invoke-Webrequest -URI $myURI; 
    $all = $req.Content;

    $shortFloat = foreach($i in ($all.split($OFS))) {if ($i -like '*Short Float*' ) {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}}; 
    if ($shortFloat -eq '') {$shortFloat = foreach($i in ($all.split($OFS))) {if ($i -like '*Short Float*' ) {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}}; }

    $EPSnextY = foreach($i in ($all.split($OFS))) {if ($i -like '*EPS next Y*' -and $i -like '*%<*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $shortRatio = foreach($i in ($all.split($OFS))) {if ($i -like '*Short Ratio*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};

    $rsi = foreach($i in ($all.split($OFS))) {if ($i -like '*RSI (14*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    if ($rsi -eq '') { $rsi = foreach($i in ($all.split($OFS))) {if ($i -like '*RSI (14*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};}

    $price = foreach($i in ($all.split($OFS))) {if ($i -like '*>Price<*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $weekPerf = foreach($i in ($all.split($OFS))) {if ($i -like '*Perf Week*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $targetPrice = foreach($i in ($all.split($OFS))) {if ($i -like '*Target Price*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $change = foreach($i in ($all.split($OFS))) {if ($i -like '*>Change<*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $insTrans = foreach($i in ($all.split($OFS))) {if ($i -like '*Insider Trans*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $instTrans = foreach($i in ($all.split($OFS))) {if ($i -like '*Inst Trans*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
                                
    $relVolume = foreach($i in ($all.split($OFS))) {if ($i -like '*Rel Vol*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $200SMA = foreach($i in ($all.split($OFS))) {if ($i -like '*SMA200*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $50SMA = foreach($i in ($all.split($OFS))) {if ($i -like '*SMA50*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $20SMA = foreach($i in ($all.split($OFS))) {if ($i -like '*SMA20*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};
    $salesQoQ = foreach($i in ($all.split($OFS))) {if ($i -like '*RSI (14*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $insiderOwnership = foreach($i in ($all.split($OFS))) {if ($i -like '*>Insider Own<*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $institutionOwnership = foreach($i in ($all.split($OFS))) {if ($i -like '*Inst Own*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $anaRecom = foreach($i in ($all.split($OFS))) {if ($i -like '*Recom*') {((($i.Split('/')[1]).split('<'))[2]).split('>')[1]}};
    $anaTarget = foreach($i in ($all.split($OFS))) {if ($i -like '*Target Price*') {((($i.Split('/')[1]).split('<'))[3]).split('>')[1]}};

    $price = [decimal]$price.replace($OFS,'');
    $weekPerf = [decimal]$weekPerf.replace($OFS,'');
    $targetPrice = [decimal]$targetPrice.replace($OFS,'');
    $change = [decimal]$change.replace($OFS,'');
    $insTrans = [decimal]$insTrans.replace($OFS,'');
    $instTrans = [decimal]$instTrans.replace($OFS,'');
    $rsi = [decimal]$rsi.replace($OFS,'');
    $relVolume = [decimal]$relVolume.replace($OFS,'');
    $200SMA = [decimal]$200SMA.replace($OFS,'');
    $50SMA = [decimal]$50SMA.replace($OFS,'');
    $20SMA = [decimal]$20SMA.replace($OFS,'');
    $salesQoQ = [decimal]$salesQoQ.replace($OFS,'');
    $insiderOwnership = [decimal]$insiderOwnership.replace($OFS,'');
    $institutionOwnership = [decimal]$institutionOwnership.replace($OFS,'');
    $anaRecom = [decimal]$anaRecom.replace($OFS,'');
    $anaTarget = [decimal]$anaTarget.replace($OFS,'');
    ###
    $posSize = 0.00;
    if ( ($relVolume -gt 0 -and $relVolume -lt 2) -and $rsi -lt 60 -and $change -lt 3 -and $weekPerf -lt 5) {
        $posSize = 1;
                                
        if (((($curSym.Split('=')[1]).trim()).REPLACE(' ', '')) -notlike '\d') {
            if (((($curSym.Split('=')[1]).trim()).REPLACE(' ', '')) -notin (ForEach-Object {($todaysBuys).Split(',') | Group-Object | select count, name | Where-Object {$_.count -gt 2}})) {                            
                if ($posSize -gt 0) {
                    $totalPositionSize = $totalPositionSize + $posSize; 
                    $buyComment = ('#!>Buy: '+((($curSym.Split('=')[1]).trim()).REPLACE(' ', ''))+' | Size: '+$posSize) 
                    $buyComment | Out-File ($mainOutputFile) -Append;
                    ("time.sleep(11)") | Out-File ($mainOutputFile) -Append;                                             
                    ('rs.order_buy_fractional_by_price("'+((($curSym.Split('=')[1]).trim()).REPLACE(' ', ''))+'"'+', '+$posSize+', timeInForce='+'"'+$timeinforce+'"'+', priceType='+'"'+$priceType+'", extendedHours=True)')| Out-File ($mainOutputFile) -Append;
                    $newBuys = ($newBuys + ((($curSym.Split('=')[1]).trim()).REPLACE(' ', '')).replace($OFS, '')+',');
                    $curSymbol = ((($curSym.Split('=')[1]).trim()).REPLACE(' ', '')); 
                    $dayte = (Get-Date -Format 'MM.dd.yyyy')
                            Write-Host $dayte                
        
                        #get equityTemplate.py
                            $cntnt = gc D:\Scripts\!PowerShell\robin_stocks-master\equityBuilderTemplate.py
                        #replace *!TEMPSYM!* with $curSymbol 
                            $replacedCNTNT = $cntnt.Replace('!TEMPSYM!',$curSymbol)
                        #save file to D:\!dump as 'equityBot_<Date>_$curSymbol.py'
                            $replacedCNTNT | Out-File ('D:\!dump\equityBot_'+$dayte+'_'+$curSymbol+'.py') -Encoding utf8
                        #issue Start-Process python.exe -ArgumentList ('D:\!dump\equityBot_<Date>_$curSymbol.py');
                            Start-Process python.exe -ArgumentList ('D:\!dump\equityBot_'+$dayte+'_'+$curSymbol+'.py') 
                                            
                    Write-Host ('Symbol: '+((($curSym.Split('=')[1]).trim()).REPLACE(' ', ''))+' Short Float: '+$shortFloat+' | Price (Change): '+$price+' ('+$change+') | RSI (14): '+$rsi+' | Insi Trans: '+$insTrans+' | Inst Trans: '+$instTrans+' | Institutional Ownership: '+$institutionOwnership+' | Insider Ownership: '+$insiderOwnership)
                    Write-Host ('Start Python: D:\!dump\equityBot_'+$dayte+'_'+$curSymbol+'.py') 
                    Write-Host ('>>')
                    $stMsg = (' $'+((($curSym.Split('=')[1]).trim()).REPLACE(' ', ''))+' #BTFD'+$OFS+$h)
                    #Send-TwitterStatuses_Update -status $stMsg; 
    }}}}$msgs = '';}$msgs = '';}
}

Import-Module 'D:\Scripts\!PowerShell\PSTwitterAPI-master\PSTwitterAPI';
Import-Module 'D:\Scripts\!PowerShell\PSDiscord-master';

$Uri = 'https://discord.com/api/webhooks/795151265008451595/sQj-t9_M0hrYmC_qjAgrt-KtY7ReuExNVuQrQogUQmE0wDnXSsCxxEehUZYxjIwSwFXW';

if (((Get-Date).Hour -gt 7 -and (Get-Date).Hour -lt 24)) {
    #'Kill existing equityBot Scripts'
        foreach ($i in (gcim win32_process | Where-Object {$_.path -like '*python*' -and $_.commandline -notlike '*cryptos*'})) { Stop-Process -Id $i.ProcessId -Force}

    #'Delete old Scripts from GitHub Repository and Copy files to Repository'
        foreach ($r in (gci D:\!dump | Where-Object {$_.Name -like '*equityBot*' -or $_.Name -like '*.stocks.*'})) { Remove-Item $r.FullName -Force}
            
    #'Generate equityBots' 
        Start-Process python.exe -ArgumentList 'D:\Scripts\!PowerShell\robin_stocks-master\equityBuilder_AAPL.py'
        Start-Process python.exe -ArgumentList 'D:\Scripts\!PowerShell\robin_stocks-master\equityBuilder_MSFT.py'
        Start-Process python.exe -ArgumentList 'D:\Scripts\!PowerShell\robin_stocks-master\equityBuilder_TSLA.py'
        startEquityBots;

    #'Copy files to Repository'
        foreach ($r in (gci C:\Users\admin\Documents\GitHub\botStuff\ | Where-Object {$_.Name -like '*equityBot*' -or $_.Name -like '*.stocks.*'})) { Remove-Item $r.FullName -Force}
            foreach ($k in (gci D:\!dump\ | Where-Object {$_.fullname -like ('*equityBot_'+$dayte+'_*.py')})) { Copy-Item -Path $k.fullname -Destination ('C:\Users\admin\Documents\GitHub\botStuff\'+$k.name) }
        foreach ($r in (gci D:\Scripts\!PowerShell\robin_stocks-master | Where-Object {$_.Name -like '*equityBot*' -or $_.Name -like '*.stocks.*'})) { Remove-Item $r.FullName -Force}
            foreach ($k in (gci D:\!dump\ | Where-Object {$_.fullname -like ('*equityBot_'+$dayte+'_*.py')})) { Copy-Item -Path $k.fullname -Destination ('D:\Scripts\!PowerShell\robin_stocks-master\'+$k.name) }
    
    #'Push to GitHub'
        cd 'C:\Users\admin\Documents\GitHub\botStuff\'; 
        git push; 
            
    #'Send Message for Pi-Pulls'
        Write-Host 'equityBots Updated - Please Perform the git pull > reboot > run Sequence on all Pi Boards'
        
} else {
    Write-Host 'Outside Timeframe for equityBot'
} 