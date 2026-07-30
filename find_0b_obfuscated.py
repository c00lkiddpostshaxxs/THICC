_IOllI1OOI0ll=__import__('hashlib')
_0l1ll1lI0lIl11111='https://pyobfuscate.com'
_lOI01O0OO1l1ll=_IOllI1OOI0ll.sha256(_0l1ll1lI0lIl11111.encode('utf-8')).digest()
def _O1lO0OI0I11(_1O0Ol0OIIO0l,_l0Ol0lIl0l00Il):
	_lOl0lIOlll=bytearray();_01OI11O0Ol=0
	while len(_lOl0lIOlll)<_1O0Ol0OIIO0l:_lOl0lIOlll+=_IOllI1OOI0ll.sha256(_l0Ol0lIl0l00Il+_01OI11O0Ol.to_bytes(8,'big')).digest();_01OI11O0Ol+=1
	return bytes(_lOl0lIOlll[:_1O0Ol0OIIO0l])
_11lIOlO0OlIII101={}
def _lO1IlOO111(_00l1OIIO0O11,_00Il0O00II010lllI0):
	_Ol10lIO0101l01IOI0=_00l1OIIO0O11,_00Il0O00II010lllI0
	if _Ol10lIO0101l01IOI0 in _11lIOlO0OlIII101:return _11lIOlO0OlIII101[_Ol10lIO0101l01IOI0]
	_I0l11O1lO0I1OlOl1=bytes(_01llIOOI0O11lOI^_llIII00l1lOl10 for(_01llIOOI0O11lOI,_llIII00l1lOl10)in zip(_00l1OIIO0O11,_O1lO0OI0I11(len(_00l1OIIO0O11),_00Il0O00II010lllI0+_lOI01O0OO1l1ll))).decode('utf-8','surrogatepass');_11lIOlO0OlIII101[_Ol10lIO0101l01IOI0]=_I0l11O1lO0I1OlOl1;return _I0l11O1lO0I1OlOl1
def _llII0O11O000lIl(_0l01Ol0I0Il11I,_OO1llIIl01):
	_ll00llOOO0O=_0l01Ol0I0Il11I,_OO1llIIl01
	if _ll00llOOO0O in _11lIOlO0OlIII101:return _11lIOlO0OlIII101[_ll00llOOO0O]
	_11I01O0l0l1OII0=bytes(_1I0IIl000I1I001^_111OIOlOlIOlOIll for(_1I0IIl000I1I001,_111OIOlOlIOlOIll)in zip(_0l01Ol0I0Il11I,_O1lO0OI0I11(len(_0l01Ol0I0Il11I),_lOI01O0OO1l1ll[::-1]+_OO1llIIl01))).decode('utf-8','surrogatepass');_11lIOlO0OlIII101[_ll00llOOO0O]=_11I01O0l0l1OII0;return _11I01O0l0l1OII0
def _O0OllOOOlOl(_lOOIIO00l1O11II1OI,_1OlOOI110Il):
	_1lO10OI10OI10I0lI=_lOOIIO00l1O11II1OI,_1OlOOI110Il
	if _1lO10OI10OI10I0lI in _11lIOlO0OlIII101:return _11lIOlO0OlIII101[_1lO10OI10OI10I0lI]
	_lll0ll0OII=bytes(_11lOIIllOOl1l0l11I^_0IOOlI1l010ll1 for(_11lOIIllOOl1l0l11I,_0IOOlI1l010ll1)in zip(_lOOIIO00l1O11II1OI,_O1lO0OI0I11(len(_lOOIIO00l1O11II1OI),_lOI01O0OO1l1ll+_1OlOOI110Il))).decode('utf-8','surrogatepass');_11lIOlO0OlIII101[_1lO10OI10OI10I0lI]=_lll0ll0OII;return _lll0ll0OII
import subprocess as _01111lI11l0OlI10,os as _OOIOI00lIOOl
_l1l0O1O1OlIl0O=_O0OllOOOlOl(b'\xb6x?\x1e\xe4',b'\xaf\xdd\xaf\xce')
_0lO0011l1II1l00lO=_O0OllOOOlOl(b'\xb1\x17\xb2c\xbc',b'\x81\xe0\xb3\x18')
_11lO000lI1IlI111=_O0OllOOOlOl(b"u'\xa1LJ",b'S\xb8\xc0\x8d')
_1lII000OlIOII=_llII0O11O000lIl(b')\xd6\x99\x95\xf3',b'\xf6\xbb\xc6\n')
_II10ll000ll1I1=_O0OllOOOlOl(b'`\x8a\x1c\xfe\x86',b'\xd2\x07I4')
_0000OllOO1IOO1OO=_lO1IlOO111(b'l"\xd4\x86\xec',b']\xa1\xc2\x01')
_0IOOO1I1lIO0O=_O0OllOOOlOl(b'\x1aP-\xf4',b'\xa3\xffI8')
_11I101I1l1Ol0=_llII0O11O000lIl(b'j\xfa%\xe1',b'x\x86\x88\x90')
try:_OOI1IO01Ol=_llII0O11O000lIl(b'\x08\xf8\xc3E',b'mn_\x97');OK=_lO1IlOO111(b'FuD',b'p \x16\xc0');_OlOI0l10Ol=_lO1IlOO111(b'\xd0\xfbo',b'h\n`\xb9');FOUND=_O0OllOOOlOl(b'iV\x95\xd1',b'D\xc9>]');_1Illl101001lI=_O0OllOOOlOl(b'\xf6\xd3\x07',b'm-\xd4#')
except:_OOI1IO01Ol=_llII0O11O000lIl(b'i]E',b'@p\x9e\xf3');OK=_O0OllOOOlOl(b'se\xf1\x9f',b'\xfd\n\xfa\x8d');_OlOI0l10Ol=_O0OllOOOlOl(b'\xc1\x90l',b'\xcc\x13\xcc\xb8');FOUND=_O0OllOOOlOl(b'fG\x89',b'\xf4\x99\x1e\xd6');_1Illl101001lI=_O0OllOOOlOl(b'\xc7\xb6\x0c',b' $#\x9d')
seek=0x7fff5db66ea800
step=0x9184e72a000
_10I0I1IO01l10IO100=_OOIOI00lIOOl.path.expanduser(_O0OllOOOlOl(b'\x99[\x8azn\x7f\xc0V\xac-W\xd0\xdd\xca\x01\xf7I,+1\x9c\xd9\xd3g',b'<\x15\xe08'))
_lIOI1O1l1I=None
print(f"\n{_11I101I1l1Ol0}{_II10ll000ll1I1}{_OOI1IO01Ol} Finding MAX SPARSE FILE SIZE on your Mac...{_0IOOO1I1lIO0O}\n")
print(f"{_1lII000OlIOII}Starting seek: {seek:,}{_0IOOO1I1lIO0O}")
print(f"{_1lII000OlIOII}Initial step: {step:,}{_0IOOO1I1lIO0O}\n")
while step>=1:
	_01111lI11l0OlI10.run(f"rm -f {_10I0I1IO01l10IO100}",shell=True,capture_output=True);_0100llO01IO0OI00=_01111lI11l0OlI10.run(f"dd if=/dev/zero of={_10I0I1IO01l10IO100} bs=1 count=0 seek={seek}",shell=True,capture_output=True,text=True)
	if _O0OllOOOlOl(b'^\xdf<R\xbc]\x1b\x0b)\xa7\xeb\x86G\x9f',b'0\xdf\xd7\xb7')in _0100llO01IO0OI00.stderr or _0100llO01IO0OI00.returncode!=0:print(f"{_0lO0011l1II1l00lO}{_OlOI0l10Ol} HIT LIMIT at seek={seek:,} (step={step:,}){_0IOOO1I1lIO0O}");seek-=step;step//=10
	else:
		print(f"{_l1l0O1O1OlIl0O}{OK}{ seek=:,} → OK{_0IOOO1I1lIO0O} {_0000OllOO1IOO1OO}(step={step:,}){_0IOOO1I1lIO0O}");_lIOI1O1l1I=seek;seek+=step
		if step==1 and _lIOI1O1l1I is not None:print(f"\n{_11lO000lI1IlI111}{FOUND} FOUND LIMIT!{_0IOOO1I1lIO0O}\n");break
_1000IIOlI01O10l=_lIOI1O1l1I/1024**5
print(f"{_11I101I1l1Ol0}{_1lII000OlIOII}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{_0IOOO1I1lIO0O}")
print(f"{_11I101I1l1Ol0}{_l1l0O1O1OlIl0O}{_1Illl101001lI} PERFECT 0B LIMIT: {_lIOI1O1l1I:,} bytes{_0IOOO1I1lIO0O}")
print(f"{_11I101I1l1Ol0}{_II10ll000ll1I1}That's ~{_1000IIOlI01O10l:.3f} PB{_0IOOO1I1lIO0O}")
print(f"{_11I101I1l1Ol0}{_1lII000OlIOII}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{_0IOOO1I1lIO0O}\n")
print(f"{_11lO000lI1IlI111}Create it with:{_0IOOO1I1lIO0O}")
print(f"{_11I101I1l1Ol0}dd if=/dev/zero of=~/Downloads/THICC.sparse bs=1 count=0 seek={_lIOI1O1l1I}{_0IOOO1I1lIO0O}\n")