from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
import numpy as np

app = Flask(__name__)
CORS(app)

stock_lists = {
    "NIFTY100": [
        "ABB.NS",
        "ADANIENSOL.NS",
        "ADANIENT.NS",
        "ADANIGREEN.NS",
        "ADANIPORTS.NS",
        "ADANIPOWER.NS",
        "ATGL.NS",
        "AMBUJACEM.NS",
        "APOLLOHOSP.NS",
        "ASIANPAINT.NS",
        "DMART.NS",
        "AXISBANK.NS",
        "BAJAJ-AUTO.NS",
        "BAJFINANCE.NS",
        "BAJAJFINSV.NS",
        "BAJAJHLDNG.NS",
        "BANKBARODA.NS",
        "BERGEPAINT.NS",
        "BEL.NS",
        "BPCL.NS",
        "BHARTIARTL.NS",
        "BOSCHLTD.NS",
        "BRITANNIA.NS",
        "CANBK.NS",
        "CHOLAFIN.NS",
        "CIPLA.NS",
        "COALINDIA.NS",
        "COLPAL.NS",
        "DLF.NS",
        "DABUR.NS",
        "DIVISLAB.NS",
        "DRREDDY.NS",
        "EICHERMOT.NS",
        "GAIL.NS",
        "GODREJCP.NS",
        "GRASIM.NS",
        "HCLTECH.NS",
        "HDFCBANK.NS",
        "HDFCLIFE.NS",
        "HAVELLS.NS",
        "HEROMOTOCO.NS",
        "HINDALCO.NS",
        "HAL.NS",
        "HINDUNILVR.NS",
        "ICICIBANK.NS",
        "ICICIGI.NS",
        "ICICIPRULI.NS",
        "ITC.NS",
        "IOC.NS",
        "IRCTC.NS",
        "IRFC.NS",
        "INDUSINDBK.NS",
        "NAUKRI.NS",
        "INFY.NS",
        "INDIGO.NS",
        "JSWSTEEL.NS",
        "JINDALSTEL.NS",
        "JIOFIN.NS",
        "KOTAKBANK.NS",
        "LTIM.NS",
        "LT.NS",
        "LICI.NS",
        "M&M.NS",
        "MARICO.NS",
        "MARUTI.NS",
        "NTPC.NS",
        "NESTLEIND.NS",
        "ONGC.NS",
        "PIDILITIND.NS",
        "PFC.NS",
        "POWERGRID.NS",
        "PNB.NS",
        "RECLTD.NS",
        "RELIANCE.NS",
        "SBICARD.NS",
        "SBILIFE.NS",
        "SRF.NS",
        "MOTHERSON.NS",
        "SHREECEM.NS",
        "SHRIRAMFIN.NS",
        "SIEMENS.NS",
        "SBIN.NS",
        "SUNPHARMA.NS",
        "TVSMOTOR.NS",
        "TCS.NS",
        "TATACONSUM.NS",
        "TATAMTRDVR.NS",
        "TATAMOTORS.NS",
        "TATAPOWER.NS",
        "TATASTEEL.NS",
        "TECHM.NS",
        "TITAN.NS",
        "TORNTPHARM.NS",
        "TRENT.NS",
        "ULTRACEMCO.NS",
        "UNITDSPR.NS",
        "VBL.NS",
        "VEDL.NS",
        "WIPRO.NS",
        "ZOMATO.NS",
        "ZYDUSLIFE.NS",
    ],
    "NIFTY200": [
        "ABB.NS",
        "ACC.NS",
        "APLAPOLLO.NS",
        "AUBANK.NS",
        "ADANIENSOL.NS",
        "ADANIENT.NS",
        "ADANIGREEN.NS",
        "ADANIPORTS.NS",
        "ADANIPOWER.NS",
        "ATGL.NS",
        "ABCAPITAL.NS",
        "ABFRL.NS",
        "ALKEM.NS",
        "AMBUJACEM.NS",
        "APOLLOHOSP.NS",
        "APOLLOTYRE.NS",
        "ASHOKLEY.NS",
        "ASIANPAINT.NS",
        "ASTRAL.NS",
        "AUROPHARMA.NS",
        "DMART.NS",
        "AXISBANK.NS",
        "BSE.NS",
        "BAJAJ-AUTO.NS",
        "BAJFINANCE.NS",
        "BAJAJFINSV.NS",
        "BAJAJHLDNG.NS",
        "BALKRISIND.NS",
        "BANDHANBNK.NS",
        "BANKBARODA.NS",
        "BANKINDIA.NS",
        "MAHABANK.NS",
        "BERGEPAINT.NS",
        "BDL.NS",
        "BEL.NS",
        "BHARATFORG.NS",
        "BHEL.NS",
        "BPCL.NS",
        "BHARTIARTL.NS",
        "BIOCON.NS",
        "BOSCHLTD.NS",
        "BRITANNIA.NS",
        "CGPOWER.NS",
        "CANBK.NS",
        "CHOLAFIN.NS",
        "CIPLA.NS",
        "COALINDIA.NS",
        "COFORGE.NS",
        "COLPAL.NS",
        "CONCOR.NS",
        "CUMMINSIND.NS",
        "DLF.NS",
        "DABUR.NS",
        "DALBHARAT.NS",
        "DEEPAKNTR.NS",
        "DELHIVERY.NS",
        "DIVISLAB.NS",
        "DIXON.NS",
        "LALPATHLAB.NS",
        "DRREDDY.NS",
        "EICHERMOT.NS",
        "ESCORTS.NS",
        "NYKAA.NS",
        "FEDERALBNK.NS",
        "FACT.NS",
        "FORTIS.NS",
        "GAIL.NS",
        "GMRINFRA.NS",
        "GLAND.NS",
        "GODREJCP.NS",
        "GODREJPROP.NS",
        "GRASIM.NS",
        "GUJGASLTD.NS",
        "HCLTECH.NS",
        "HDFCAMC.NS",
        "HDFCBANK.NS",
        "HDFCLIFE.NS",
        "HAVELLS.NS",
        "HEROMOTOCO.NS",
        "HINDALCO.NS",
        "HAL.NS",
        "HINDPETRO.NS",
        "HINDUNILVR.NS",
        "ICICIBANK.NS",
        "ICICIGI.NS",
        "ICICIPRULI.NS",
        "IDBI.NS",
        "IDFCFIRSTB.NS",
        "ITC.NS",
        "INDIANB.NS",
        "INDHOTEL.NS",
        "IOC.NS",
        "IRCTC.NS",
        "IRFC.NS",
        "IGL.NS",
        "INDUSTOWER.NS",
        "INDUSINDBK.NS",
        "NAUKRI.NS",
        "INFY.NS",
        "INDIGO.NS",
        "IPCALAB.NS",
        "JSWENERGY.NS",
        "JSWINFRA.NS",
        "JSWSTEEL.NS",
        "JINDALSTEL.NS",
        "JIOFIN.NS",
        "JUBLFOOD.NS",
        "KPITTECH.NS",
        "KALYANKJIL.NS",
        "KOTAKBANK.NS",
        "LTF.NS",
        "LTTS.NS",
        "LICHSGFIN.NS",
        "LTIM.NS",
        "LT.NS",
        "LAURUSLABS.NS",
        "LICI.NS",
        "LUPIN.NS",
        "MRF.NS",
        "LODHA.NS",
        "M&MFIN.NS",
        "M&M.NS",
        "MANKIND.NS",
        "MARICO.NS",
        "MARUTI.NS",
        "MFSL.NS",
        "MAXHEALTH.NS",
        "MAZDOCK.NS",
        "MPHASIS.NS",
        "NHPC.NS",
        "NMDC.NS",
        "NTPC.NS",
        "NESTLEIND.NS",
        "OBEROIRLTY.NS",
        "ONGC.NS",
        "OIL.NS",
        "PAYTM.NS",
        "OFSS.NS",
        "POLICYBZR.NS",
        "PIIND.NS",
        "PAGEIND.NS",
        "PATANJALI.NS",
        "PERSISTENT.NS",
        "PETRONET.NS",
        "PIDILITIND.NS",
        "PEL.NS",
        "POLYCAB.NS",
        "POONAWALLA.NS",
        "PFC.NS",
        "POWERGRID.NS",
        "PRESTIGE.NS",
        "PNB.NS",
        "RECLTD.NS",
        "RVNL.NS",
        "RELIANCE.NS",
        "SBICARD.NS",
        "SBILIFE.NS",
        "SJVN.NS",
        "SRF.NS",
        "MOTHERSON.NS",
        "SHREECEM.NS",
        "SHRIRAMFIN.NS",
        "SIEMENS.NS",
        "SONACOMS.NS",
        "SBIN.NS",
        "SAIL.NS",
        "SUNPHARMA.NS",
        "SUNTV.NS",
        "SUPREMEIND.NS",
        "SUZLON.NS",
        "SYNGENE.NS",
        "TVSMOTOR.NS",
        "TATACHEM.NS",
        "TATACOMM.NS",
        "TCS.NS",
        "TATACONSUM.NS",
        "TATAELXSI.NS",
        "TATAMTRDVR.NS",
        "TATAMOTORS.NS",
        "TATAPOWER.NS",
        "TATASTEEL.NS",
        "TATATECH.NS",
        "TECHM.NS",
        "TITAN.NS",
        "TORNTPHARM.NS",
        "TORNTPOWER.NS",
        "TRENT.NS",
        "TIINDIA.NS",
        "UPL.NS",
        "ULTRACEMCO.NS",
        "UNIONBANK.NS",
        "UNITDSPR.NS",
        "VBL.NS",
        "VEDL.NS",
        "IDEA.NS",
        "VOLTAS.NS",
        "WIPRO.NS",
        "YESBANK.NS",
        "ZEEL.NS",
        "ZOMATO.NS",
        "ZYDUSLIFE.NS",
    ],
    "NIFTY500": [
        "360ONE.NS",
        "3MINDIA.NS",
        "ABB.NS",
        "ACC.NS",
        "AIAENG.NS",
        "APLAPOLLO.NS",
        "AUBANK.NS",
        "AARTIIND.NS",
        "AAVAS.NS",
        "ABBOTINDIA.NS",
        "ACE.NS",
        "ADANIENSOL.NS",
        "ADANIENT.NS",
        "ADANIGREEN.NS",
        "ADANIPORTS.NS",
        "ADANIPOWER.NS",
        "ATGL.NS",
        "AWL.NS",
        "ABCAPITAL.NS",
        "ABFRL.NS",
        "AEGISLOG.NS",
        "AETHER.NS",
        "AFFLE.NS",
        "AJANTPHARM.NS",
        "APLLTD.NS",
        "ALKEM.NS",
        "ALKYLAMINE.NS",
        "ALLCARGO.NS",
        "ALOKINDS.NS",
        "ARE&M.NS",
        "AMBER.NS",
        "AMBUJACEM.NS",
        "ANANDRATHI.NS",
        "ANGELONE.NS",
        "ANURAS.NS",
        "APARINDS.NS",
        "APOLLOHOSP.NS",
        "APOLLOTYRE.NS",
        "APTUS.NS",
        "ACI.NS",
        "ASAHIINDIA.NS",
        "ASHOKLEY.NS",
        "ASIANPAINT.NS",
        "ASTERDM.NS",
        "ASTRAZEN.NS",
        "ASTRAL.NS",
        "ATUL.NS",
        "AUROPHARMA.NS",
        "AVANTIFEED.NS",
        "DMART.NS",
        "AXISBANK.NS",
        "BEML.NS",
        "BLS.NS",
        "BSE.NS",
        "BAJAJ-AUTO.NS",
        "BAJFINANCE.NS",
        "BAJAJFINSV.NS",
        "BAJAJHLDNG.NS",
        "BALAMINES.NS",
        "BALKRISIND.NS",
        "BALRAMCHIN.NS",
        "BANDHANBNK.NS",
        "BANKBARODA.NS",
        "BANKINDIA.NS",
        "MAHABANK.NS",
        "BATAINDIA.NS",
        "BAYERCROP.NS",
        "BERGEPAINT.NS",
        "BDL.NS",
        "BEL.NS",
        "BHARATFORG.NS",
        "BHEL.NS",
        "BPCL.NS",
        "BHARTIARTL.NS",
        "BIKAJI.NS",
        "BIOCON.NS",
        "BIRLACORPN.NS",
        "BSOFT.NS",
        "BLUEDART.NS",
        "BLUESTARCO.NS",
        "BBTC.NS",
        "BORORENEW.NS",
        "BOSCHLTD.NS",
        "BRIGADE.NS",
        "BRITANNIA.NS",
        "MAPMYINDIA.NS",
        "CCL.NS",
        "CESC.NS",
        "CGPOWER.NS",
        "CIEINDIA.NS",
        "CRISIL.NS",
        "CSBBANK.NS",
        "CAMPUS.NS",
        "CANFINHOME.NS",
        "CANBK.NS",
        "CAPLIPOINT.NS",
        "CGCL.NS",
        "CARBORUNIV.NS",
        "CASTROLIND.NS",
        "CEATLTD.NS",
        "CELLO.NS",
        "CENTRALBK.NS",
        "CDSL.NS",
        "CENTURYPLY.NS",
        "CENTURYTEX.NS",
        "CERA.NS",
        "CHALET.NS",
        "CHAMBLFERT.NS",
        "CHEMPLASTS.NS",
        "CHENNPETRO.NS",
        "CHOLAHLDNG.NS",
        "CHOLAFIN.NS",
        "CIPLA.NS",
        "CUB.NS",
        "CLEAN.NS",
        "COALINDIA.NS",
        "COCHINSHIP.NS",
        "COFORGE.NS",
        "COLPAL.NS",
        "CAMS.NS",
        "CONCORDBIO.NS",
        "CONCOR.NS",
        "COROMANDEL.NS",
        "CRAFTSMAN.NS",
        "CREDITACC.NS",
        "CROMPTON.NS",
        "CUMMINSIND.NS",
        "CYIENT.NS",
        "DCMSHRIRAM.NS",
        "DLF.NS",
        "DOMS.NS",
        "DABUR.NS",
        "DALBHARAT.NS",
        "DATAPATTNS.NS",
        "DEEPAKFERT.NS",
        "DEEPAKNTR.NS",
        "DELHIVERY.NS",
        "DEVYANI.NS",
        "DIVISLAB.NS",
        "DIXON.NS",
        "LALPATHLAB.NS",
        "DRREDDY.NS",
        "EIDPARRY.NS",
        "EIHOTEL.NS",
        "EPL.NS",
        "EASEMYTRIP.NS",
        "EICHERMOT.NS",
        "ELECON.NS",
        "ELGIEQUIP.NS",
        "EMAMILTD.NS",
        "ENDURANCE.NS",
        "ENGINERSIN.NS",
        "EQUITASBNK.NS",
        "ERIS.NS",
        "ESCORTS.NS",
        "EXIDEIND.NS",
        "FDC.NS",
        "NYKAA.NS",
        "FEDERALBNK.NS",
        "FACT.NS",
        "FINEORG.NS",
        "FINCABLES.NS",
        "FINPIPE.NS",
        "FSL.NS",
        "FIVESTAR.NS",
        "FORTIS.NS",
        "GAIL.NS",
        "GMMPFAUDLR.NS",
        "GMRINFRA.NS",
        "GRSE.NS",
        "GICRE.NS",
        "GILLETTE.NS",
        "GLAND.NS",
        "GLAXO.NS",
        "GLS.NS",
        "GLENMARK.NS",
        "MEDANTA.NS",
        "GPIL.NS",
        "GODFRYPHLP.NS",
        "GODREJCP.NS",
        "GODREJIND.NS",
        "GODREJPROP.NS",
        "GRANULES.NS",
        "GRAPHITE.NS",
        "GRASIM.NS",
        "GESHIP.NS",
        "GRINDWELL.NS",
        "GAEL.NS",
        "FLUOROCHEM.NS",
        "GUJGASLTD.NS",
        "GMDCLTD.NS",
        "GNFC.NS",
        "GPPL.NS",
        "GSFC.NS",
        "GSPL.NS",
        "HEG.NS",
        "HBLPOWER.NS",
        "HCLTECH.NS",
        "HDFCAMC.NS",
        "HDFCBANK.NS",
        "HDFCLIFE.NS",
        "HFCL.NS",
        "HAPPSTMNDS.NS",
        "HAPPYFORGE.NS",
        "HAVELLS.NS",
        "HEROMOTOCO.NS",
        "HSCL.NS",
        "HINDALCO.NS",
        "HAL.NS",
        "HINDCOPPER.NS",
        "HINDPETRO.NS",
        "HINDUNILVR.NS",
        "HINDZINC.NS",
        "POWERINDIA.NS",
        "HOMEFIRST.NS",
        "HONASA.NS",
        "HONAUT.NS",
        "HUDCO.NS",
        "ICICIBANK.NS",
        "ICICIGI.NS",
        "ICICIPRULI.NS",
        "ISEC.NS",
        "IDBI.NS",
        "IDFCFIRSTB.NS",
        "IDFC.NS",
        "IIFL.NS",
        "IRB.NS",
        "IRCON.NS",
        "ITC.NS",
        "ITI.NS",
        "INDIACEM.NS",
        "IBULHSGFIN.NS",
        "INDIAMART.NS",
        "INDIANB.NS",
        "IEX.NS",
        "INDHOTEL.NS",
        "IOC.NS",
        "IOB.NS",
        "IRCTC.NS",
        "IRFC.NS",
        "INDIGOPNTS.NS",
        "IGL.NS",
        "INDUSTOWER.NS",
        "INDUSINDBK.NS",
        "NAUKRI.NS",
        "INFY.NS",
        "INOXWIND.NS",
        "INTELLECT.NS",
        "INDIGO.NS",
        "IPCALAB.NS",
        "JBCHEPHARM.NS",
        "JKCEMENT.NS",
        "JBMA.NS",
        "JKLAKSHMI.NS",
        "JKPAPER.NS",
        "JMFINANCIL.NS",
        "JSWENERGY.NS",
        "JSWINFRA.NS",
        "JSWSTEEL.NS",
        "JAIBALAJI.NS",
        "J&KBANK.NS",
        "JINDALSAW.NS",
        "JSL.NS",
        "JINDALSTEL.NS",
        "JIOFIN.NS",
        "JUBLFOOD.NS",
        "JUBLINGREA.NS",
        "JUBLPHARMA.NS",
        "JWL.NS",
        "JUSTDIAL.NS",
        "JYOTHYLAB.NS",
        "KPRMILL.NS",
        "KEI.NS",
        "KNRCON.NS",
        "KPITTECH.NS",
        "KRBL.NS",
        "KSB.NS",
        "KAJARIACER.NS",
        "KPIL.NS",
        "KALYANKJIL.NS",
        "KANSAINER.NS",
        "KARURVYSYA.NS",
        "KAYNES.NS",
        "KEC.NS",
        "KFINTECH.NS",
        "KOTAKBANK.NS",
        "KIMS.NS",
        "LTF.NS",
        "LTTS.NS",
        "LICHSGFIN.NS",
        "LTIM.NS",
        "LT.NS",
        "LATENTVIEW.NS",
        "LAURUSLABS.NS",
        "LXCHEM.NS",
        "LEMONTREE.NS",
        "LICI.NS",
        "LINDEINDIA.NS",
        "LLOYDSME.NS",
        "LUPIN.NS",
        "MMTC.NS",
        "MRF.NS",
        "MTARTECH.NS",
        "LODHA.NS",
        "MGL.NS",
        "MAHSEAMLES.NS",
        "M&MFIN.NS",
        "M&M.NS",
        "MHRIL.NS",
        "MAHLIFE.NS",
        "MANAPPURAM.NS",
        "MRPL.NS",
        "MANKIND.NS",
        "MARICO.NS",
        "MARUTI.NS",
        "MASTEK.NS",
        "MFSL.NS",
        "MAXHEALTH.NS",
        "MAZDOCK.NS",
        "MEDPLUS.NS",
        "METROBRAND.NS",
        "METROPOLIS.NS",
        "MINDACORP.NS",
        "MSUMI.NS",
        "MOTILALOFS.NS",
        "MPHASIS.NS",
        "MCX.NS",
        "MUTHOOTFIN.NS",
        "NATCOPHARM.NS",
        "NBCC.NS",
        "NCC.NS",
        "NHPC.NS",
        "NLCINDIA.NS",
        "NMDC.NS",
        "NSLNISP.NS",
        "NTPC.NS",
        "NH.NS",
        "NATIONALUM.NS",
        "NAVINFLUOR.NS",
        "NESTLEIND.NS",
        "NETWORK18.NS",
        "NAM-INDIA.NS",
        "NUVAMA.NS",
        "NUVOCO.NS",
        "OBEROIRLTY.NS",
        "ONGC.NS",
        "OIL.NS",
        "OLECTRA.NS",
        "PAYTM.NS",
        "OFSS.NS",
        "POLICYBZR.NS",
        "PCBL.NS",
        "PIIND.NS",
        "PNBHOUSING.NS",
        "PNCINFRA.NS",
        "PVRINOX.NS",
        "PAGEIND.NS",
        "PATANJALI.NS",
        "PERSISTENT.NS",
        "PETRONET.NS",
        "PHOENIXLTD.NS",
        "PIDILITIND.NS",
        "PEL.NS",
        "PPLPHARMA.NS",
        "POLYMED.NS",
        "POLYCAB.NS",
        "POONAWALLA.NS",
        "PFC.NS",
        "POWERGRID.NS",
        "PRAJIND.NS",
        "PRESTIGE.NS",
        "PRINCEPIPE.NS",
        "PRSMJOHNSN.NS",
        "PGHH.NS",
        "PNB.NS",
        "QUESS.NS",
        "RRKABEL.NS",
        "RBLBANK.NS",
        "RECLTD.NS",
        "RHIM.NS",
        "RITES.NS",
        "RADICO.NS",
        "RVNL.NS",
        "RAILTEL.NS",
        "RAINBOW.NS",
        "RAJESHEXPO.NS",
        "RKFORGE.NS",
        "RCF.NS",
        "RATNAMANI.NS",
        "RTNINDIA.NS",
        "RAYMOND.NS",
        "REDINGTON.NS",
        "RELIANCE.NS",
        "RBA.NS",
        "ROUTE.NS",
        "SBFC.NS",
        "SBICARD.NS",
        "SBILIFE.NS",
        "SJVN.NS",
        "SKFINDIA.NS",
        "SRF.NS",
        "SAFARI.NS",
        "MOTHERSON.NS",
        "SANOFI.NS",
        "SAPPHIRE.NS",
        "SAREGAMA.NS",
        "SCHAEFFLER.NS",
        "SCHNEIDER.NS",
        "SHREECEM.NS",
        "RENUKA.NS",
        "SHRIRAMFIN.NS",
        "SHYAMMETL.NS",
        "SIEMENS.NS",
        "SIGNATURE.NS",
        "SOBHA.NS",
        "SOLARINDS.NS",
        "SONACOMS.NS",
        "SONATSOFTW.NS",
        "STARHEALTH.NS",
        "SBIN.NS",
        "SAIL.NS",
        "SWSOLAR.NS",
        "STLTECH.NS",
        "SUMICHEM.NS",
        "SPARC.NS",
        "SUNPHARMA.NS",
        "SUNTV.NS",
        "SUNDARMFIN.NS",
        "SUNDRMFAST.NS",
        "SUNTECK.NS",
        "SUPREMEIND.NS",
        "SUVENPHAR.NS",
        "SUZLON.NS",
        "SWANENERGY.NS",
        "SYNGENE.NS",
        "SYRMA.NS",
        "TV18BRDCST.NS",
        "TVSMOTOR.NS",
        "TVSSCS.NS",
        "TMB.NS",
        "TANLA.NS",
        "TATACHEM.NS",
        "TATACOMM.NS",
        "TCS.NS",
        "TATACONSUM.NS",
        "TATAELXSI.NS",
        "TATAINVEST.NS",
        "TATAMTRDVR.NS",
        "TATAMOTORS.NS",
        "TATAPOWER.NS",
        "TATASTEEL.NS",
        "TATATECH.NS",
        "TTML.NS",
        "TECHM.NS",
        "TEJASNET.NS",
        "NIACL.NS",
        "RAMCOCEM.NS",
        "THERMAX.NS",
        "TIMKEN.NS",
        "TITAGARH.NS",
        "TITAN.NS",
        "TORNTPHARM.NS",
        "TORNTPOWER.NS",
        "TRENT.NS",
        "TRIDENT.NS",
        "TRIVENI.NS",
        "TRITURBINE.NS",
        "TIINDIA.NS",
        "UCOBANK.NS",
        "UNOMINDA.NS",
        "UPL.NS",
        "UTIAMC.NS",
        "UJJIVANSFB.NS",
        "ULTRACEMCO.NS",
        "UNIONBANK.NS",
        "UBL.NS",
        "UNITDSPR.NS",
        "USHAMART.NS",
        "VGUARD.NS",
        "VIPIND.NS",
        "VAIBHAVGBL.NS",
        "VTL.NS",
        "VARROC.NS",
        "VBL.NS",
        "MANYAVAR.NS",
        "VEDL.NS",
        "VIJAYA.NS",
        "IDEA.NS",
        "VOLTAS.NS",
        "WELCORP.NS",
        "WELSPUNLIV.NS",
        "WESTLIFE.NS",
        "WHIRLPOOL.NS",
        "WIPRO.NS",
        "YESBANK.NS",
        "ZFCVINDIA.NS",
        "ZEEL.NS",
        "ZENSARTECH.NS",
        "ZOMATO.NS",
        "ZYDUSLIFE.NS",
        "ECLERX.NS",
    ],
}


def calculate_gross_return(stock_symbol, period, block_size):
    data = yf.download(tickers=stock_symbol, period=f"{period}d")["Adj Close"]

    blocks = data.resample(f"{block_size}D")

    total_pct_change = 1.0

    for name, group in blocks:
        if not group.empty:
            start_price = group.iloc[0]
            end_price = group.iloc[-1]
            pct_change = (end_price / start_price - 1) * 100

            total_pct_change *= 1 + pct_change / 100
            print(group)

    overall_pct_change = (total_pct_change - 1) * 100

    return overall_pct_change


@app.route("/analyze/<stock_list>", methods=["POST"])
def analyze_stocks(stock_list):
    if stock_list not in stock_lists:
        return jsonify({"error": "Invalid stock list"}), 400

    request_data = request.json
    period = int(request_data["period"])
    block_size = int(request_data["blockSize"])

    stock_symbols = stock_lists[stock_list]

    results = []
    for symbol in stock_symbols:
        returns = calculate_gross_return(symbol, period, block_size)
        results.append({"symbol": symbol, "returns": returns})

    results.sort(key=lambda x: x["returns"], reverse=True)

    returns_sorted = [r["returns"] for r in results]
    deciles = np.percentile(returns_sorted, [10, 20, 30, 40, 50, 60, 70, 80, 90])

    decile_labels = [
        "Decile 1",
        "Decile 2",
        "Decile 3",
        "Decile 4",
        "Decile 5",
        "Decile 6",
        "Decile 7",
        "Decile 8",
        "Decile 9",
        "Decile 10",
    ]
    decile_results = [[] for _ in range(10)]

    for stock in results:
        returns = stock["returns"]
        if returns >= deciles[8]:
            decile_index = 0
        elif returns >= deciles[7]:
            decile_index = 1
        elif returns >= deciles[6]:
            decile_index = 2
        elif returns >= deciles[5]:
            decile_index = 3
        elif returns >= deciles[4]:
            decile_index = 4
        elif returns >= deciles[3]:
            decile_index = 5
        elif returns >= deciles[2]:
            decile_index = 6
        elif returns >= deciles[1]:
            decile_index = 7
        elif returns >= deciles[0]:
            decile_index = 8
        else:
            decile_index = 9

        decile_results[decile_index].append(stock)

    response_data = {
        "deciles": [
            {"label": label, "stocks": decile}
            for label, decile in zip(decile_labels, decile_results)
        ]
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
