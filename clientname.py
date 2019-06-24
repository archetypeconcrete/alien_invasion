import json

users = ['Vladimirov.L', 'smirnova.m', 'kenig.g', 'arzhadeeva.e', 'ipatov.a', 'blokhina.n', 'dyachkov.p',
         'kolesnikov.d', 'kryukov.d', 'ippolitov.a', 'kozlov.s', 'bogdanov.v', 'korotkov.k',
         'stepanenko.a', 'lukoyanova.t', 'labinskiy.a', 'zavyalov.a', 'sukhoterin.e', 'popova.a', 'kuznetsova.e',
         'pesochenko.v', 'tashkaev.i', 'lovyagina.m', 'parubin.v', 'leonteva.a',
         'maksimova.a', 'demyanenko.v', 'spirina.a', 'duhovskoj.v', 'konev.d', 'biryukov.m', 'klein.a', 'galyaveev.n',
         'kim.a', 'beskrovnyj.s', 'kochadykov.v',
         'shabashkin.o', 'sokolov.p', 'shlepnev.a', 'dyakov.i', 'torgashev.d', 'shirokov.a', 'emelyanova.d', 'popov.m',
         'haritonov.g', 'shchyuchkin.e', 'chechyotkin.y', 'chichvarin.v',
         'gutor.a', 'komarova.e', 'blyakherov.d', 'dorokhin.s', 'ukharov.p', 'udodova.e', 'osipov.v', 'shumilov.e',
         'knyazev.k', 'gridin.u', 'tihonov.d', 'kirillov.a', 'vlasov.d',
         'belyakov.d', 'devlikanova.s', 'shabunin.d', 'ipatova.e', 'reshetnikov.i', 'bakanov.e', 'panfilov.a',
         'votyakov.t', 'grigorev.a', 'ragimov.i', 'ermilova.u', 'anisimova.r',
         'ilinova.e', 'kovalev.g', 'shumilov.n', 'uvarkin.g', 'malinin.p', 'braslavets.d', 'panukov.a', 'novikov.m',
         'benevolenskiy.d', 'bolshakov.k', 'pavlov.v', 'gorochnyy.v',
         'voronin.a', 'zubkov.a', 'bobkov.vd', 'egorov.d', 'shilyaev.a', 'germanov.r', 'kosolapov.m', 'kaptunov.a',
         'leybovich.u', 'mikhailov.a', 'zhukov.m', 'arkhipov.v',
         'huzina.s', 'vernidub.m', 'makarov.e', 'bobrov.v', 'petushin.k', 'frolova.i', 'voronina.e', 'yagupov.m',
         'romanov.r', 'dolgov.a', 'fisher.a', 'artemeva.o', 'bahovskiy.v',
         'cshevelev.a', 'gurev.i', 'devyatova.p', 'bosuk.a', 'antonov.d', 'mahotin.k', 'gavrin.a', 'antonova.l',
         'livitskiy.d', 'tsukanov.p']

for username in users:

    u_path = "\\" + "\\" + "milandr01" + "\\" + "Home" + "\\" + username + "\\" + username + "\\" + "Chrome" + "\\" + "Local State"
    # print(u_path)
    try:
        with open(u_path, 'r') as f:
            data = f.read()
            d = json.loads(data)
            d["browser"]["enabled_labs_experiments"] = ["expensive-background-timer-throttling@1",
                                                        "stop-non-timers-in-background@1"]
    except FileNotFoundError:
        msg = " " + username + " DOES not exist."
        print(msg)
    else:
        with open(u_path, 'r+') as f:
            f.write(json.dumps(d))
            # print('Done - ' + username)
