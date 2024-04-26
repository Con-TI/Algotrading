import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

label_fontsize = 8
stock_codes = ['AALI.JK', 'ABBA.JK', 'ABDA.JK', 'ABMM.JK', 'ACES.JK', 'ACST.JK', 'ADCP.JK', 'ADES.JK', 'ADHI.JK', 'ADMF.JK', 'ADMG.JK', 'ADMR.JK', 'ADRO.JK', 'AEGS.JK', 'AGAR.JK', 'AGII.JK', 'AGRO.JK', 'AGRS.JK', 'AHAP.JK', 'AIMS.JK', 'AISA.JK', 'AKKU.JK', 'AKPI.JK', 'AKRA.JK', 'AKSI.JK', 'ALDO.JK', 'ALKA.JK', 'ALMI.JK', 'ALTO.JK', 'AMAG.JK', 'AMAN.JK', 'AMAR.JK', 'AMFG.JK', 'AMIN.JK', 'AMMN.JK', 'AMMS.JK', 'AMOR.JK', 'AMRT.JK', 'ANDI.JK', 'ANJT.JK', 'ANTM.JK', 'APEX.JK', 'APIC.JK', 'APII.JK', 'APLI.JK', 'APLN.JK', 'ARCI.JK', 'ARGO.JK', 'ARII.JK', 'ARKA.JK', 'ARKO.JK', 'ARNA.JK', 'ARTA.JK', 'ARTI.JK', 'ARTO.JK', 'ASBI.JK', 'ASDM.JK', 'ASGR.JK', 'ASHA.JK', 'ASII.JK', 'ASJT.JK', 'ASLC.JK', 'ASMI.JK', 'ASPI.JK', 'ASRI.JK', 'ASRM.JK', 'ASSA.JK', 'ATAP.JK', 'ATIC.JK', 'AUTO.JK', 'AVIA.JK', 'AWAN.JK', 'AXIO.JK', 'AYAM.JK', 'AYLS.JK', 'BABP.JK', 'BABY.JK', 'BACA.JK', 'BAJA.JK', 'BALI.JK', 'BANK.JK', 'BAPA.JK', 'BATA.JK', 'BAUT.JK', 'BAYU.JK', 'BBCA.JK', 'BBHI.JK', 'BBKP.JK', 'BBLD.JK', 'BBMD.JK', 'BBNI.JK', 'BBRI.JK', 'BBRM.JK', 'BBSI.JK', 'BBSS.JK', 'BBTN.JK', 'BBYB.JK', 'BCAP.JK', 'BCIC.JK', 'BCIP.JK', 'BDKR.JK', 'BDMN.JK', 'BEBS.JK', 'BEEF.JK', 'BEER.JK', 'BEKS.JK', 'BELI.JK', 'BELL.JK', 'BESS.JK', 'BEST.JK', 'BFIN.JK', 'BGTG.JK', 'BHAT.JK', 'BHIT.JK', 'BIKA.JK', 'BIKE.JK', 'BIMA.JK', 'BINA.JK', 'BINO.JK', 'BIPI.JK', 'BIPP.JK', 'BIRD.JK', 'BISI.JK', 'BJBR.JK', 'BJTM.JK', 'BKDP.JK', 'BKSL.JK', 'BKSW.JK', 'BLTA.JK', 'BLTZ.JK', 'BLUE.JK', 'BMAS.JK', 'BMBL.JK', 'BMHS.JK', 'BMRI.JK', 'BMSR.JK', 'BMTR.JK', 'BNBA.JK', 'BNBR.JK', 'BNGA.JK', 'BNII.JK', 'BNLI.JK', 'BOBA.JK', 'BOGA.JK', 'BOLA.JK', 'BOLT.JK', 'BPFI.JK', 'BPII.JK', 'BPTR.JK', 'BRAM.JK', 'BREN.JK', 'BRIS.JK', 'BRMS.JK', 'BRNA.JK', 'BRPT.JK', 'BSBK.JK', 'BSDE.JK', 'BSIM.JK', 'BSML.JK', 'BSSR.JK', 'BSWD.JK', 'BTEK.JK', 'BTON.JK', 'BTPN.JK', 'BTPS.JK', 'BUAH.JK', 'BUDI.JK', 'BUKA.JK', 'BUKK.JK', 'BULL.JK', 'BUMI.JK', 'BUVA.JK', 'BVIC.JK', 'BWPT.JK', 'BYAN.JK', 'CAKK.JK', 'CAMP.JK', 'CANI.JK', 'CARE.JK', 'CARS.JK', 'CASA.JK', 'CASH.JK', 'CASS.JK', 'CBPE.JK', 'CBRE.JK', 'CBUT.JK', 'CCSI.JK', 'CEKA.JK', 'CENT.JK', 'CFIN.JK', 'CHEM.JK', 'CHIP.JK', 'CINT.JK', 'CITA.JK', 'CITY.JK', 'CLEO.JK', 'CLPI.JK', 'CMNP.JK', 'CMNT.JK', 'CMPP.JK', 'CMRY.JK', 'CNKO.JK', 'CNMA.JK', 'CNTX.JK', 'COAL.JK', 'COCO.JK', 'CPIN.JK', 'CPRO.JK', 'CRAB.JK', 'CRSN.JK', 'CSAP.JK', 'CSIS.JK', 'CSMI.JK', 'CSRA.JK', 'CTBN.JK', 'CTRA.JK', 'CTTH.JK', 'CUAN.JK', 'CYBR.JK', 'DADA.JK', 'DART.JK', 'DAYA.JK', 'DCII.JK', 'DEPO.JK', 'DEWA.JK', 'DEWI.JK', 'DFAM.JK', 'DGIK.JK', 'DGNS.JK', 'DIGI.JK', 'DILD.JK', 'DIVA.JK', 'DKFT.JK', 'DLTA.JK', 'DMAS.JK', 'DMMX.JK', 'DMND.JK', 'DNAR.JK', 'DNET.JK', 'DOID.JK', 'DOOH.JK', 'DPNS.JK', 'DPUM.JK', 'DRMA.JK', 'DSFI.JK', 'DSNG.JK', 'DSSA.JK', 'DUTI.JK', 'DVLA.JK', 'DWGL.JK', 'DYAN.JK', 'EAST.JK', 'ECII.JK', 'EDGE.JK', 'EKAD.JK', 'ELIT.JK', 'ELPI.JK', 'ELSA.JK', 'ELTY.JK', 'EMDE.JK', 'EMTK.JK', 'ENAK.JK', 'ENRG.JK', 'ENZO.JK', 'EPAC.JK', 'EPMT.JK', 'ERAA.JK', 'ERAL.JK', 'ERTX.JK', 'ESIP.JK', 'ESSA.JK', 'ESTA.JK', 'ESTI.JK', 'EURO.JK', 'EXCL.JK', 'FAPA.JK', 'FAST.JK', 'FASW.JK', 'FILM.JK', 'FIMP.JK', 'FIRE.JK', 'FISH.JK', 'FITT.JK', 'FLMC.JK', 'FMII.JK', 'FOLK.JK', 'FOOD.JK', 'FPNI.JK', 'FREN.JK', 'FUJI.JK', 'FUTR.JK', 'FWCT.JK', 'GDST.JK', 'GDYR.JK', 'GEMA.JK', 'GEMS.JK', 'GGRM.JK', 'GGRP.JK', 'GHON.JK', 'GIAA.JK', 'GJTL.JK', 'GLOB.JK', 'GLVA.JK', 'GMFI.JK', 'GMTD.JK', 'GOLD.JK', 'GOOD.JK', 'GOTO.JK', 'GPRA.JK', 'GPSO.JK', 'GRIA.JK', 'GRPM.JK', 'GSMF.JK', 'GTBO.JK', 'GTRA.JK', 'GTSI.JK', 'GULA.JK', 'GWSA.JK', 'GZCO.JK', 'HADE.JK', 'HAIS.JK', 'HAJJ.JK', 'HALO.JK', 'HATM.JK', 'HBAT.JK', 'HDFA.JK', 'HDIT.JK', 'HEAL.JK', 'HELI.JK', 'HERO.JK', 'HEXA.JK', 'HILL.JK', 'HITS.JK', 'HMSP.JK', 'HOKI.JK', 'HOMI.JK', 'HOPE.JK', 'HRME.JK', 'HRTA.JK', 'HRUM.JK', 'HUMI.JK', 'IATA.JK', 'IBFN.JK', 'IBOS.JK', 'IBST.JK', 'ICBP.JK', 'ICON.JK', 'IDEA.JK', 'IDPR.JK', 'IFII.JK', 'IFSH.JK', 'IGAR.JK', 'IKAI.JK', 'IKAN.JK', 'IKBI.JK', 'IKPM.JK', 'IMAS.JK', 'IMJS.JK', 'IMPC.JK', 'INAF.JK', 'INAI.JK', 'INCF.JK', 'INCI.JK', 'INCO.JK', 'INDF.JK', 'INDO.JK', 'INDR.JK', 'INDS.JK', 'INDX.JK', 'INDY.JK', 'INET.JK', 'INKP.JK', 'INOV.JK', 'INPC.JK', 'INPP.JK', 'INPS.JK', 'INRU.JK', 'INTA.JK', 'INTD.JK', 'INTP.JK', 'IOTF.JK', 'IPAC.JK', 'IPCC.JK', 'IPCM.JK', 'IPOL.JK', 'IPPE.JK', 'IPTV.JK', 'IRRA.JK', 'IRSX.JK', 'ISAP.JK', 'ISAT.JK', 'ISSP.JK', 'ITIC.JK', 'ITMA.JK', 'ITMG.JK', 'JARR.JK', 'JAST.JK', 'JATI.JK', 'JAWA.JK', 'JAYA.JK', 'JECC.JK', 'JGLE.JK', 'JIHD.JK', 'JKON.JK', 'JMAS.JK', 'JPFA.JK', 'JRPT.JK', 'JSMR.JK', 'JSPT.JK', 'JTPE.JK', 'KAEF.JK', 'KARW.JK', 'KAYU.JK', 'KBAG.JK', 'KBLI.JK', 'KBLM.JK', 'KBLV.JK', 'KDSI.JK', 'KDTN.JK', 'KEEN.JK', 'KEJU.JK', 'KETR.JK', 'KIAS.JK', 'KICI.JK', 'KIJA.JK', 'KING.JK', 'KINO.JK', 'KIOS.JK', 'KJEN.JK', 'KKES.JK', 'KKGI.JK', 'KLAS.JK', 'KLBF.JK', 'KLIN.JK', 'KMDS.JK', 'KMTR.JK', 'KOBX.JK', 'KOCI.JK', 'KOIN.JK', 'KOKA.JK', 'KONI.JK', 'KOPI.JK', 'KOTA.JK', 'KPIG.JK', 'KRAS.JK', 'KREN.JK', 'KRYA.JK', 'KUAS.JK', 'LABA.JK', 'LAJU.JK', 'LAND.JK', 'LAPD.JK', 'LCKM.JK', 'LEAD.JK', 'LFLO.JK', 'LIFE.JK', 'LINK.JK', 'LION.JK', 'LMAX.JK', 'LMPI.JK', 'LMSH.JK', 'LOPI.JK', 'LPCK.JK', 'LPGI.JK', 'LPIN.JK', 'LPKR.JK', 'LPLI.JK', 'LPPF.JK', 'LPPS.JK', 'LRNA.JK', 'LSIP.JK', 'LTLS.JK', 'LUCK.JK', 'LUCY.JK', 'MAHA.JK', 'MAIN.JK', 'MAPA.JK', 'MAPB.JK', 'MAPI.JK', 'MARI.JK', 'MARK.JK', 'MASA.JK', 'MASB.JK', 'MAXI.JK', 'MAYA.JK', 'MBAP.JK', 'MBMA.JK', 'MBSS.JK', 'MBTO.JK', 'MCAS.JK', 'MCOL.JK', 'MCOR.JK', 'MDIA.JK', 'MDKA.JK', 'MDKI.JK', 'MDLN.JK', 'MDRN.JK', 'MEDC.JK', 'MEDS.JK', 'MEGA.JK', 'MENN.JK', 'MERK.JK', 'MFIN.JK', 'MFMI.JK', 'MGLV.JK', 'MGNA.JK', 'MGRO.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MINA.JK', 'MIRA.JK', 'MITI.JK', 'MKNT.JK', 'MKPI.JK', 'MKTR.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMIX.JK', 'MMLP.JK', 'MNCN.JK', 'MOLI.JK', 'MORA.JK', 'MPMX.JK', 'MPOW.JK', 'MPPA.JK', 'MPRO.JK', 'MPXL.JK', 'MRAT.JK', 'MREI.JK', 'MSIE.JK', 'MSIN.JK', 'MSKY.JK', 'MSTI.JK', 'MTDL.JK', 'MTEL.JK', 'MTLA.JK', 'MTMH.JK', 'MTPS.JK', 'MTSM.JK', 'MTWI.JK', 'MUTU.JK', 'MYOH.JK', 'MYOR.JK', 'MYTX.JK', 'NANO.JK', 'NASA.JK', 'NASI.JK', 'NATO.JK', 'NAYZ.JK', 'NCKL.JK', 'NELY.JK', 'NETV.JK', 'NFCX.JK', 'NICK.JK', 'NICL.JK', 'NIKL.JK', 'NINE.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NPGF.JK', 'NRCA.JK', 'NSSS.JK', 'NTBK.JK', 'NZIA.JK', 'OASA.JK', 'OBMD.JK', 'OILS.JK', 'OKAS.JK', 'OLIV.JK', 'OMED.JK', 'OMRE.JK', 'OPMS.JK', 'PACK.JK', 'PADA.JK', 'PADI.JK', 'PALM.JK', 'PAMG.JK', 'PANI.JK', 'PANR.JK', 'PANS.JK', 'PBID.JK', 'PBRX.JK', 'PBSA.JK', 'PCAR.JK', 'PDES.JK', 'PDPP.JK', 'PEGE.JK', 'PEHA.JK', 'PEVE.JK', 'PGAS.JK', 'PGEO.JK', 'PGJO.JK', 'PGLI.JK', 'PGUN.JK', 'PICO.JK', 'PIPA.JK', 'PJAA.JK', 'PKPK.JK', 'PLAN.JK', 'PLIN.JK', 'PMJS.JK', 'PMMP.JK', 'PNBN.JK', 'PNBS.JK', 'PNGO.JK', 'PNIN.JK', 'PNLF.JK', 'POLA.JK', 'POLI.JK', 'POLL.JK', 'POLU.JK', 'POLY.JK', 'PORT.JK', 'POWR.JK', 'PPGL.JK', 'PPRE.JK', 'PPRI.JK', 'PPRO.JK', 'PRAY.JK', 'PRDA.JK', 'PRIM.JK', 'PSAB.JK', 'PSDN.JK', 'PSGO.JK', 'PSKT.JK', 'PSSI.JK', 'PTBA.JK', 'PTDU.JK', 'PTIS.JK', 'PTMP.JK', 'PTPP.JK', 'PTPS.JK', 'PTPW.JK', 'PTRO.JK', 'PTSN.JK', 'PTSP.JK', 'PUDP.JK', 'PURA.JK', 'PURI.JK', 'PWON.JK', 'PYFA.JK', 'PZZA.JK', 'RAAM.JK', 'RAFI.JK', 'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RCCC.JK', 'RDTX.JK', 'REAL.JK', 'RELF.JK', 'RELI.JK', 'RGAS.JK', 'RICY.JK', 'RIGS.JK', 'RISE.JK', 'RMKE.JK', 'RMKO.JK', 'ROCK.JK', 'RODA.JK', 'RONY.JK', 'ROTI.JK', 'RSCH.JK', 'RSGK.JK', 'RUIS.JK', 'RUNS.JK', 'SAFE.JK', 'SAGE.JK', 'SAME.JK', 'SAMF.JK', 'SAPX.JK', 'SATU.JK', 'SBAT.JK', 'SBMA.JK', 'SCCO.JK', 'SCMA.JK', 'SCNP.JK', 'SCPI.JK', 'SDMU.JK', 'SDPC.JK', 'SDRA.JK', 'SEMA.JK', 'SFAN.JK', 'SGER.JK', 'SGRO.JK', 'SHID.JK', 'SHIP.JK', 'SICO.JK', 'SIDO.JK', 'SILO.JK', 'SIMP.JK', 'SINI.JK', 'SIPD.JK', 'SKBM.JK', 'SKLT.JK', 'SKRN.JK', 'SLIS.JK', 'SMAR.JK', 'SMBR.JK', 'SMCB.JK', 'SMDM.JK', 'SMDR.JK', 'SMGR.JK', 'SMIL.JK', 'SMKL.JK', 'SMKM.JK', 'SMMA.JK', 'SMMT.JK', 'SMRA.JK', 'SMSM.JK', 'SNLK.JK', 'SOCI.JK', 'SOFA.JK', 'SOHO.JK', 'SONA.JK', 'SOSS.JK', 'SOTS.JK', 'SOUL.JK', 'SPMA.JK', 'SPTO.JK', 'SQMI.JK', 'SRAJ.JK', 'SRSN.JK', 'SRTG.JK', 'SSIA.JK', 'SSMS.JK', 'SSTM.JK', 'STAA.JK', 'STAR.JK', 'STRK.JK', 'STTP.JK', 'SULI.JK', 'SUNI.JK', 'SURE.JK', 'SURI.JK', 'SWAT.JK', 'SWID.JK', 'TALF.JK', 'TAMA.JK', 'TAPG.JK', 'TARA.JK', 'TAXI.JK', 'TAYS.JK', 'TBIG.JK', 'TBLA.JK', 'TBMS.JK', 'TCID.JK', 'TCPI.JK', 'TEBE.JK', 'TELE.JK', 'TFAS.JK', 'TFCO.JK', 'TGKA.JK', 'TGRA.JK', 'TGUK.JK', 'TIFA.JK', 'TINS.JK', 'TIRA.JK', 'TIRT.JK', 'TKIM.JK', 'TLDN.JK', 'TLKM.JK', 'TMAS.JK', 'TMPO.JK', 'TNCA.JK', 'TOBA.JK', 'TOOL.JK', 'TOPS.JK', 'TOTL.JK', 'TOTO.JK', 'TOWR.JK', 'TOYS.JK', 'TPIA.JK', 'TPMA.JK', 'TRGU.JK', 'TRIM.JK', 'TRIN.JK', 'TRIS.JK', 'TRJA.JK', 'TRON.JK', 'TRST.JK', 'TRUE.JK', 'TRUK.JK', 'TRUS.JK', 'TSPC.JK', 'TUGU.JK', 'TYRE.JK', 'UANG.JK', 'UCID.JK', 'UDNG.JK', 'UFOE.JK', 'ULTJ.JK', 'UNIC.JK', 'UNIQ.JK', 'UNSP.JK', 'UNTR.JK', 'UNVR.JK', 'URBN.JK', 'UVCR.JK', 'VAST.JK', 'VICI.JK', 'VICO.JK', 'VINS.JK', 'VIVA.JK', 'VKTR.JK', 'VOKS.JK', 'VRNA.JK', 'VTNY.JK', 'WAPO.JK', 'WEGE.JK', 'WEHA.JK', 'WGSH.JK', 'WICO.JK', 'WIDI.JK', 'WIFI.JK', 'WIIM.JK', 'WINE.JK', 'WINR.JK', 'WINS.JK', 'WIRG.JK', 'WMPP.JK', 'WMUU.JK', 'WOMF.JK', 'WOOD.JK', 'WOWS.JK', 'WSBP.JK', 'WTON.JK', 'YELO.JK', 'YPAS.JK', 'YULE.JK', 'ZATA.JK', 'ZBRA.JK', 'ZINC.JK', 'ZONE.JK', 'ZYRX.JK']
filtered_data = pd.read_pickle('../Data_Collection/clean_data_5min.pkl')

def has_consecutive_repeats(column, num_of_repeat):
    prev_value = None
    consecutive_count = 1
    for value in column:
        if value == prev_value:
            consecutive_count += 1
            if consecutive_count > num_of_repeat:
                return True
        else:
            consecutive_count = 1
        prev_value = value
    return False

list_of_flat_stocks = []
for column in filtered_data['Close'].columns:
    current_series = filtered_data['Close'][column]
    if has_consecutive_repeats(current_series, 30):
        list_of_flat_stocks.append(column)

filtered_codes = [code for code in stock_codes if code not in list_of_flat_stocks]
filtered_data = filtered_data.tz_convert('Asia/Jakarta')
filtered_data = filtered_data[2:-1]
daily_dataframes = [group[:-1] for _,group in filtered_data.groupby(pd.Grouper(freq='D')) if not group.empty]

class Data:
    def __init__(self):
        self.minimum_times = []
        self.num_times = []
        self.how_much_lower = []
        self.high_low_spreads = []

neg = Data()
pos = Data()
neutral = Data()

def reference_time_session(date):
    return pd.to_datetime(f'{date} 12:00:00+07:00')

def reference_time(date, hour,minute):
    return pd.to_datetime(f'{date} {hour}:{minute}:00+07:00')

def convert(date):
    return pd.to_datetime(f'{date} ')

threshold = 2


for code in filtered_codes:
    for group in daily_dataframes:
        current_date = group.index[0].strftime('%Y-%m-%d')
        change_in_first_hour = 100*(group['Open'][code].iloc[0] - group['Close'][code].iloc[11])/group['Open'][code].iloc[0]
        low_series = group['Low'][code]
        high_series = group['High'][code]
        minimum = low_series.min()
        minimum_time = low_series.idxmin()
        number_of_times_hit_minimum = len(low_series[low_series==minimum])
        # print(number_of_times_hit_minimum)
        ten_oclock = reference_time(current_date, 10, 00)
        if change_in_first_hour > threshold:
            pos.minimum_times.append(minimum_time)
            if minimum_time < ten_oclock:
                filtered_high = high_series[high_series.index >= minimum_time]
                high_low_spread = (filtered_high.max()-minimum)/minimum
                pos.high_low_spreads.append(high_low_spread)
                pos.num_times.append(number_of_times_hit_minimum)
            if minimum_time > ten_oclock:
                minimum_in_first_hour = low_series[:12].min()
                change_from_low_to_further_low =(minimum - minimum_in_first_hour)/minimum_in_first_hour
                pos.how_much_lower.append(change_from_low_to_further_low)
        elif change_in_first_hour < -threshold:
            neg.minimum_times.append(minimum_time)
            if minimum_time < ten_oclock:
                filtered_high = high_series[high_series.index >= minimum_time]
                high_low_spread = (filtered_high.max() - minimum) / minimum
                neg.high_low_spreads.append(high_low_spread)
                neg.num_times.append(number_of_times_hit_minimum)
            if minimum_time > ten_oclock:
                minimum_in_first_hour = low_series[:12].min()
                change_from_low_to_further_low = (minimum - minimum_in_first_hour) / minimum_in_first_hour
                neg.how_much_lower.append(change_from_low_to_further_low)
        else:
            neutral.minimum_times.append(minimum_time)
            if minimum_time < ten_oclock:
                filtered_high = high_series[high_series.index >= minimum_time]
                high_low_spread = (filtered_high.max() - minimum) / minimum
                neutral.high_low_spreads.append(high_low_spread)
                neutral.num_times.append(number_of_times_hit_minimum)
            if minimum_time > ten_oclock:
                minimum_in_first_hour = low_series[:12].min()
                change_from_low_to_further_low = (minimum - minimum_in_first_hour) / minimum_in_first_hour
                neutral.how_much_lower.append(change_from_low_to_further_low)


def to_hour_values(list):
    datetimed = pd.to_datetime(list, format='%H:%M')
    return [time.hour+time.minute/60 for time in datetimed]

figure = plt.figure(figsize=(10,6))
grid = plt.GridSpec(nrows=3,ncols=6)

neg_min_times = figure.add_subplot(grid[0,0])
sns.kdeplot(to_hour_values(neg.minimum_times),ax=neg_min_times)
neg_min_times.set_title(f'(Neg)\nfirst hr chg < -{threshold}')
neg_min_times.set_xlabel('Time')
neutral_min_times = figure.add_subplot(grid[0,2])
sns.kdeplot(to_hour_values(neutral.minimum_times),ax=neutral_min_times)
neutral_min_times.set_title(f'(Neutral)\n-{threshold} < first hr chg < {threshold}')
neutral_min_times.set_xlabel('Time')
pos_min_times = figure.add_subplot(grid[0,4])
sns.kdeplot(to_hour_values(pos.minimum_times),ax=pos_min_times)
pos_min_times.set_title(f'(Pos)\n{threshold} < first hr chg')
pos_min_times.set_xlabel('Time')

neg_if_low_aft_first_hour_how_much_lower = figure.add_subplot(grid[0,1])
sns.kdeplot(neg.how_much_lower,ax=neg_if_low_aft_first_hour_how_much_lower)
neg_if_low_aft_first_hour_how_much_lower.set_title('(Neg) How much lower \n if low is later')
neg_if_low_aft_first_hour_how_much_lower.set_xlabel('Pct from low in first hour')
neutral_if_low_aft_first_hour_how_much_lower = figure.add_subplot(grid[0,3])
sns.kdeplot(neutral.how_much_lower,ax=neutral_if_low_aft_first_hour_how_much_lower)
neutral_if_low_aft_first_hour_how_much_lower.set_title('(Neutral) How much lower \n if low is later')
neutral_if_low_aft_first_hour_how_much_lower.set_xlabel('Pct from low in first hour')
pos_if_low_aft_first_hour_how_much_lower = figure.add_subplot(grid[0,5])
sns.kdeplot(pos.how_much_lower,ax=pos_if_low_aft_first_hour_how_much_lower)
pos_if_low_aft_first_hour_how_much_lower.set_title('(Pos) How much lower \n if low is later')
pos_if_low_aft_first_hour_how_much_lower.set_xlabel('Pct from low in first hour')

neg_high_low_spreads_if_bef_first_hr = figure.add_subplot(grid[1,0])
sns.kdeplot(neg.high_low_spreads,ax=neg_high_low_spreads_if_bef_first_hr)
neg_high_low_spreads_if_bef_first_hr.set_title('(Neg) High Low Spreads\n if low is earlier')
neg_high_low_spreads_if_bef_first_hr.set_xlabel('Pct from low')
neutral_high_low_spreads_if_bef_first_hr = figure.add_subplot(grid[1,2])
sns.kdeplot(neutral.high_low_spreads,ax=neutral_high_low_spreads_if_bef_first_hr)
neutral_high_low_spreads_if_bef_first_hr.set_title('(Neutral) High Low Spreads\n if low is earlier')
neutral_high_low_spreads_if_bef_first_hr.set_xlabel('Pct from low')
pos_high_low_spreads_if_bef_first_hr = figure.add_subplot(grid[1,4])
sns.kdeplot(pos.high_low_spreads,ax=pos_high_low_spreads_if_bef_first_hr)
pos_high_low_spreads_if_bef_first_hr.set_title('(Pos) High Low Spreads\n if low is earlier')
pos_high_low_spreads_if_bef_first_hr.set_xlabel('Pct from low')



fig_mgr = plt.get_current_fig_manager()
fig_mgr.window.wm_geometry("+0+0")
plt.tight_layout()
plt.subplots_adjust(right=0.9)
plt.show()