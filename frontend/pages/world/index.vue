<template>
  <v-layout justify-center align-center>
    <template>
      <v-container class="contmapa">
        <geo-chart
          :data="gdata"
        />
        <div style="color: black">Países com mais mortes</div>
        <bar-chart :data="[[gdata[0][0], gdata[0][1]], [gdata[1][0], gdata[1][1]],
                           [gdata[2][0], gdata[2][1]], [gdata[3][0], gdata[3][1]], [gdata[4][0], gdata[4][1]], [gdata[5][0], gdata[5][1]]]"
        />
        <div style="color: black">Países com mais casos</div>
        <bar-chart :data="[[casos[0][0], casos[0][1]], [casos[1][0], casos[1][1]],
                           [casos[2][0], casos[2][1]], [casos[3][0], casos[3][1]], [casos[4][0], casos[4][1]], [casos[5][0], casos[5][1]]]"
        />
        <div style="color: black">Países com mais casos recuperados</div>
        <bar-chart :data="[[recuperados[0][0], recuperados[0][1]], [recuperados[1][0], recuperados[1][1]],
                           [recuperados[2][0], recuperados[2][1]], [recuperados[3][0], recuperados[3][1]], [recuperados[4][0], recuperados[4][1]], [recuperados[5][0], recuperados[5][1]]]"
        />
      </v-container>
    </template>
  </v-layout>
</template>

<script>

export default {
  data () {
    return {
      recuperados: [],
      casos: [],
      gdata: [],
      globaldata_inc: [
        {
          'infected': 106359,
          'tested': 'NA',
          'recovered': 72538,
          'deceased': 2877,
          'country': 'Algeria',
          'moreData': 'https://api.apify.com/v2/key-value-stores/pp4Wo2slUJ78ZnaAi/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/hi0DJXpcyzDwtg2Fm/items?format=json&clean=1',
          'sourceUrl': 'https://www.worldometers.info/coronavirus/',
          'lastUpdatedApify': '2021-01-28T19:55:00.000Z'
        },
        {
          'infected': 407362,
          'tested': 9089588,
          'recovered': 387787,
          'deceased': 7607,
          'country': 'Austria',
          'moreData': 'https://api.apify.com/v2/key-value-stores/RJtyHLXtCepb4aYxB/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/EFWZ2Q5JAtC6QDSwV/items?format=json&clean=1',
          'sourceUrl': 'https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 229793,
          'tested': 2387,
          'recovered': 222154,
          'deceased': 3113,
          'country': 'Azerbaijan',
          'moreData': 'https://api.apify.com/v2/key-value-stores/ThmCW2NVnrLa0tVp5/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/JtJHjnBtnIeKYpFi0/items?format=json&clean=1',
          'sourceUrl': 'https://koronavirusinfo.az/az/page/statistika/azerbaycanda-cari-veziyyet',
          'lastUpdatedSource': 'N/A',
          'lastUpdatedApify': '2021-01-28T20:00:23.000Z'
        },
        {
          'infected': 100804,
          'tested': 2660221,
          'recovered': 97337,
          'deceased': 59,
          'country': 'Bahrain',
          'moreData': 'https://api.apify.com/v2/key-value-stores/c7Bc6QnnwaPLOMv3J/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/eHhCNFErvfnC42mEc/items?format=json&clean=1',
          'sourceUrl': 'https://www.moh.gov.bh/COVID19',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 699662,
          'tested': 8035739,
          'recovered': 'NA',
          'deceased': 20933,
          'country': 'Belgium',
          'moreData': 'https://api.apify.com/v2/key-value-stores/apVM8aZ8hKZFvnKm7/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/DD9jrAixr0QMvQIE3/items?format=json&clean=1',
          'sourceUrl': 'https://epistat.wiv-isp.be/Covid',
          'lastUpdatedSource': '2021-01-27T17:12:00.000Z',
          'lastUpdatedApify': '2021-01-28T19:55:00.000Z'
        },
        {
          'infected': 8996876,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 220161,
          'country': 'Brazil',
          'moreData': 'https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/3S2T1ZBxB9zhRJTBB/items?format=json&clean=1',
          'sourceUrl': 'https://covid.saude.gov.br/',
          'lastUpdatedSource': '2021-01-28T12:47:29.756Z',
          'lastUpdatedApify': '2021-01-28T20:00:14.049Z'
        },
        {
          'infected': 217014,
          'tested': 'NA',
          'recovered': 0,
          'deceased': 8944,
          'country': 'Bulgaria',
          'moreData': 'https://api.apify.com/v2/key-value-stores/np4eYah8M5uQtj0Su/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/OicoAbu38M2cGAcDl/items?format=json&clean=1',
          'sourceUrl': 'https://coronavirus.bg/bg/',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 761226,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 19533,
          'country': 'Canada',
          'moreData': 'https://api.apify.com/v2/key-value-stores/fabbocwKrtxSDf96h/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/ji95MgtBVgGJF7XcP/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:00:19.000Z'
        },
        {
          'infected': 89326,
          'tested': 160000000,
          'recovered': 82870,
          'deceased': 4636,
          'country': 'China',
          'moreData': 'https://api.apify.com/v2/key-value-stores/x4iHxk7TVGI7UxFv6/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/LQHrXhGe0EhnCFeei/items?format=json&clean=1',
          'sourceUrl': 'https://www.worldometers.info/coronavirus/',
          'lastUpdatedApify': '2021-01-28T19:55:00.000Z'
        },
        {
          'infected': 230978,
          'tested': 'NA',
          'recovered': 222862,
          'deceased': 4,
          'country': 'Croatia',
          'moreData': ' https://api.apify.com/v2/key-value-stores/ealAQXP81dedhLWay/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/dQxN0GCqxJ1MhgLR4/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 964660,
          'tested': 4519978,
          'recovered': 851400,
          'deceased': 15944,
          'country': 'Czech Republic',
          'moreData': 'https://api.apify.com/v2/key-value-stores/K373S4uCFR9W1K8ei/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/XQWw0I5IUaUPQdc9k/items?format=json&clean=1',
          'lastUpdatedSource': '2021-01-28T06:50:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:01:00.000Z'
        },
        {
          'infected': 190619,
          'tested': 12090669,
          'recovered': 172456,
          'deceased': 1837,
          'country': 'Denmark',
          'moreData': 'https://api.apify.com/v2/key-value-stores/EAlpwScH29Qa5m60g/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/Ugq8cNqnhUSjfJeHr/items?format=json&clean=1',
          'sourceUrl': 'https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning',
          'lastUpdatedSource': '2021-01-19T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 42656,
          'tested': 760266,
          'recovered': 'NA',
          'deceased': 406,
          'country': 'Estonia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/AZUhwS51lBBg26wSG/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/Ix8h3SN2Ngyukf7yM/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T19:55:24.000Z'
        },
        {
          'infected': 44039,
          'tested': 2782,
          'recovered': 'NA',
          'deceased': 664,
          'country': 'Finland',
          'moreData': 'https://api.apify.com/v2/key-value-stores/jEFt5tgCTMfjJpLD3/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/BDEAOLx0DzEW91s5L/items?format=json&clean=1',
          'sourceUrl': 'https://thl.fi/fi/web/infektiotaudit-ja-rokotukset/ajankohtaista/ajankohtaista-koronaviruksesta-covid-19/tilannekatsaus-koronaviruksesta',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 3106859,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 74456,
          'country': 'France',
          'moreData': 'https://api.apify.com/v2/key-value-stores/ufVgKLP8ljtn3ufaU/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/QBiS7pd57KVmFfgZM/items?format=json&clean=1',
          'sourceUrl': 'https://dashboard.covid19.data.gouv.fr/',
          'lastUpdatedSource': '2021-01-27T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 2178828,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 54913,
          'country': 'Germany',
          'moreData': 'https://api.apify.com/v2/key-value-stores/OHrZyNo9BzT6xKMRD/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/dcm4uXhiGIjVdJAzS/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:02:08.000Z'
        },
        {
          'infected': 144007,
          'tested': 'NA',
          'recovered': 60669,
          'deceased': 3512,
          'country': 'Honduras',
          'moreData': 'https://api.apify.com/v2/key-value-stores/b11FFW9RA1B3gIMyg/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/VDtCgFny8WSfPStct/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 363450,
          'tested': 3097809,
          'recovered': 249003,
          'deceased': 12291,
          'country': 'Hungary',
          'moreData': 'https://api.apify.com/v2/key-value-stores/RGEUeKe60NjU16Edo/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/Gm6qjTgGqxkEZTkuJ/items?format=json&clean=1',
          'sourceUrl': 'https://koronavirus.gov.hu',
          'lastUpdatedSource': '2021-01-28T08:22:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 10701193,
          'tested': 'NA',
          'recovered': 10373606,
          'deceased': 153847,
          'country': 'India',
          'moreData': 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true',
          'historyData': ' https://api.apify.com/v2/datasets/58a4VXwBBF0HtxuQa/items?format=json&clean=1',
          'sourceUrl': 'https://www.mohfw.gov.in/',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 1398841,
          'tested': 9125076,
          'recovered': 1189975,
          'deceased': 57736,
          'country': 'Iran',
          'moreData': 'https://api.apify.com/v2/key-value-stores/XV4DWf1ctkSPA8H99/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/PJEXhmQM0hkN8K3BK/items?format=json&clean=1',
          'sourceUrl': 'https://www.worldometers.info/coronavirus/',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 2515507,
          'tested': 'NA',
          'recovered': 1953509,
          'deceased': 87381,
          'country': 'Italy',
          'moreData': 'https://api.apify.com/v2/key-value-stores/UFpnR8mukiu0TSrb4/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/CUdKmb25Z3HjkoDiN/items?format=json&clean=1',
          'sourceUrl': 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json',
          'lastUpdatedSource': '2021-01-28T17:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:19.583Z'
        },
        {
          'infected': 380600,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 5500,
          'country': 'Japan',
          'moreData': 'https://api.apify.com/v2/key-value-stores/YbboJrL3cgVfkV1am/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/ugfJOQkPhQ0fvLYzN/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:02:05.000Z'
        },
        {
          'infected': 12683,
          'tested': 'NA',
          'recovered': 8788,
          'deceased': 488,
          'country': 'Kosovo',
          'moreData': 'https://api.apify.com/v2/key-value-stores/C10heVVVE8yBd1YvF/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/ruoBcTzhMpN6SaeS2/items?format=json&clean=1',
          'sourceUrl': 'https://kosova.health/en/',
          'lastUpdatedSource': 'N/A',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 180170,
          'tested': 'NA',
          'recovered': 125067,
          'deceased': 2746,
          'country': 'Lithuania',
          'moreData': 'https://api.apify.com/v2/key-value-stores/xhGDb8VTqjtm1AQL6/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/1XdITM6u7PbhUrlmK/items?format=json&clean=1',
          'sourceUrl': 'https://osp.maps.arcgis.com/apps/MapSeries/index.html?appid=79255eaa219140dfa65c01ae95ed143b',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 49438,
          'tested': 1828776,
          'recovered': 'NA',
          'deceased': 562,
          'country': 'Luxembourg',
          'moreData': 'https://api.apify.com/v2/key-value-stores/RVkUl1Y7FZn3Y410K/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/oZH6thpQSdIyo3ky2/items?format=json&clean=1',
          'sourceUrl': 'https://data.public.lu/fr/datasets/donnees-covid19/',
          'lastUpdatedSource': '2021-01-22T17:05:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 198208,
          'tested': 'NA',
          'recovered': 154299,
          'deceased': 717,
          'country': 'Malaysia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/6t65lJVfs3d8s6aKc/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/7Fdb90FMDLZir2ROo/items?format=json&clean=1',
          'sourceUrl': 'http://covid-19.moh.gov.my/',
          'lastUpdatedSource': '2021-01-28T12:08:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 979631,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 13924,
          'country': 'Netherlands',
          'moreData': 'https://api.apify.com/v2/key-value-stores/vqnEUe7VtKNMqGqFF/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/jr5ogVGnyfMZJwpnB/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T19:55:26.000Z'
        },
        {
          'infected': 126160,
          'tested': 'NA',
          'recovered': 100365,
          'deceased': 1544,
          'country': 'Nigeria',
          'moreData': 'https://api.apify.com/v2/key-value-stores/Eb694wt67UxjdSGbc/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/ccY329O0ng68poTiX/items?format=json&clean=1',
          'sourceUrl': 'https://covid19.ncdc.gov.ng/',
          'lastUpdatedSource': 'N/A',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 61960,
          'tested': 3357400,
          'recovered': 'NA',
          'deceased': 557,
          'country': 'Norway',
          'moreData': 'https://api.apify.com/v2/key-value-stores/3qlmMu1XN2ZLoVIQt/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/6tpTe4Z2TBePRWYti/items?format=json&clean=1',
          'sourceUrl': 'https://www.fhi.no/sv/smittsomme-sykdommer/corona/dags--og-ukerapporter/dags--og-ukerapporter-om-koronavirus/',
          'lastUpdatedSource': '2021-01-28T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 539387,
          'tested': 'NA',
          'recovered': 494578,
          'deceased': 11514,
          'country': 'Pakistan',
          'moreData': 'https://api.apify.com/v2/key-value-stores/QhfG8Kj6tVYMgud6R/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/9eUGCilmJ8HDf60mL/items?format=json&clean=1',
          'sourceUrl': 'http://covid.gov.pk',
          'lastUpdatedSource': '2021-01-28T02:39:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:24.959Z'
        },
        {
          'infected': 177426,
          'tested': 4499,
          'recovered': 166441,
          'deceased': 1990,
          'country': 'Palestine',
          'moreData': 'https://api.apify.com/v2/key-value-stores/SbribCOVf2wgR868y/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/BKpHLQrJPmgXE51tf/items?format=json&clean=1',
          'sourceUrl': 'http://site.moh.ps/index/covid19/LanguageVersion/1/Language/ar',
          'lastUpdatedSource': '2021-01-28T20:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 519575,
          'tested': 'NA',
          'recovered': 475596,
          'deceased': 10552,
          'country': 'Philippines',
          'moreData': 'https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true',
          'historyData': ' https://api.apify.com/v2/datasets/sFSef5gfYg3soj8mb/items?format=json&clean=1',
          'sourceUrl': 'https://endcov.ph/dashboard/',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 1443804,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 33698,
          'country': 'Poland',
          'moreData': 'https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/L3VCmhMeX0KUQeJto/items?format=json&clean=1',
          'sourceUrl': 'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2',
          'lastUpdatedApify': '2021-01-20T09:35:00.000Z'
        },
        {
          'infected': 668951,
          'tested': 'NA',
          'recovered': 484753,
          'deceased': 11305,
          'country': 'Portugal',
          'moreData': 'https://api.apify.com/v2/key-value-stores/BXGEYTTUQzYBboEQK/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/f1Qd4cMBzV1E0oRNc/items?format=json&clean=1',
          'sourceUrl': 'https://covid19.min-saude.pt/ponto-de-situacao-atual-em-portugal/',
          'lastUpdatedSource': '2021-01-27T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T19:55:00.000Z'
        },
        {
          'infected': 721513,
          'tested': 5379447,
          'recovered': 666001,
          'deceased': 18105,
          'country': 'Romania',
          'moreData': 'https://api.apify.com/v2/key-value-stores/KUlj8EGfDGHiB0gU1/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/n1XtXTelVG5dJhDhy/items?format=json&clean=1',
          'sourceUrl': '',
          'lastUpdatedSource': '2021-01-28T13:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 3793810,
          'tested': 17803955,
          'recovered': 3229258,
          'deceased': 71651,
          'country': 'Russia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/1brJ0NLbQaJKPTWMO/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/5JO5GL1h8Qv1CnG0m/items?format=json',
          'sourceUrl': 'https://covid19.rosminzdrav.ru/',
          'lastUpdatedSource': '2021-01-28T20:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 367276,
          'tested': 'NA',
          'recovered': 358753,
          'deceased': 6366,
          'country': 'Saudi Arabia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/40xwYCZ57p5OkyBIJ/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/OeaEEGdhvUSkXRrWU/items?format=json&clean=1',
          'sourceUrl': 'https://covid19.moh.gov.sa/',
          'lastUpdatedSource': '2020-07-21T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:34.595Z'
        },
        {
          'infected': 390637,
          'tested': 2588844,
          'recovered': 382466,
          'deceased': 3965,
          'country': 'Serbia',
          'moreData': ' https://api.apify.com/v2/key-value-stores/aHENGKUPUhKlX97aL/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/X00EUFYFa9dsIdD8a/items?format=json',
          'sourceUrl': 'https://covid19.rs/homepage-english/',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 59425,
          'tested': 'NA',
          'recovered': 59148,
          'deceased': 29,
          'country': 'Singapore',
          'moreData': 'https://api.apify.com/v2/key-value-stores/yaPbKe9e5Et61bl7W/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/suHgi59tSfu02VsRO/items?format=json&clean=1',
          'sourceUrl': 'https://www.moh.gov.sg/covid-19',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 243427,
          'tested': 9811,
          'recovered': 205247,
          'deceased': 4411,
          'country': 'Slovakia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/GlTLAdXAuOz6bLAIO/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/oUWi8ci7F2R9V5ZFy/items?format=json&clean=1',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 162429,
          'tested': 1026296,
          'recovered': 'NA',
          'deceased': 3448,
          'country': 'Slovenia',
          'moreData': 'https://api.apify.com/v2/key-value-stores/603AyvQ8QjyqmnZx6/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/H6HKZRQr8I81bClnb/items?format=json&clean=1',
          'sourceUrl': 'https://www.gov.si/en/topics/coronavirus-disease-covid-19/actual-data/',
          'lastUpdatedSource': '2021-01-28T10:26:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 76926,
          'tested': 5522189,
          'recovered': 'NA',
          'deceased': 1386,
          'country': 'South Korea',
          'moreData': 'https://api.apify.com/v2/key-value-stores/TMFbhs7qtXpGpeaeP/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/Lc0Hoa8MgAbscJA4w/items?format=json&clean=1',
          'sourceUrl': 'http://ncov.mohw.go.kr/en',
          'lastUpdatedSource': '2021-01-28T12:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 2705001,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 57806,
          'country': 'Spain',
          'moreData': 'https://api.apify.com/v2/key-value-stores/lluBbYoQVN65R3BGO/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/hxwow9BB75z8RV3JT/items?format=json&clean=1',
          'sourceUrl': 'https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/situacionActual.htm',
          'lastUpdatedSource': '2021-01-28T14:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 564557,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 11520,
          'country': 'Sweden',
          'moreData': 'https://api.apify.com/v2/key-value-stores/8mRFdwyukavRNCr42/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/Nq3XwHX262iDwsFJS/items?format=json&clean=1',
          'sourceUrl': 'https://services5.arcgis.com/fsYDFeRKu1hELJJs/arcgis/rest/services/FOHM_Covid_19_FME_1/FeatureServer/0/query?f=json&where=Region%20%3C%3E%20%27dummy%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Region%20asc&outSR=102100&resultOffset=0&resultRecordCount=25&cacheHint=true',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 519404,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 8597,
          'country': 'Switzerland',
          'moreData': 'https://api.apify.com/v2/key-value-stores/lDegAca820XgvjE0C/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/73pVXuygDYAtIMOhI/items?format=json&clean=1',
          'sourceUrl': 'https://www.bag.admin.ch/bag/en/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/situation-schweiz-und-international.html',
          'lastUpdatedSource': '2021-01-28T09:19:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 2457118,
          'tested': 29181125,
          'recovered': 2340216,
          'deceased': 25605,
          'country': 'Turkey',
          'moreData': 'https://api.apify.com/v2/key-value-stores/28ljlt47S5XEd1qIi/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/LYeOfHQwsv7FsfdGV/items?format=json&clean=1',
          'sourceUrl': 'https://covid19.saglik.gov.tr/covid19api?getir=sondurum',
          'lastUpdatedSource': '2021-01-28T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 3743734,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 103602,
          'country': 'United Kingdom',
          'moreData': 'https://api.apify.com/v2/key-value-stores/KWLojgM5r1JmMW4b4/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/K1mXdufnpvr53AFk6/items?format=json&clean=1',
          'sourceUrl': 'https://coronavirus.data.gov.uk/',
          'lastUpdatedSource': '2021-01-28T16:03:18.452106Z',
          'lastUpdatedApify': '2021-01-28T20:01:00.000Z'
        },
        {
          'infected': 25456670,
          'tested': 'NA',
          'recovered': 'NA',
          'deceased': 427626,
          'country': 'United States',
          'moreData': 'https://api.apify.com/v2/key-value-stores/moxA3Q0aZh5LosewB/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/FIbyK6uHUntt2kNy3/items?format=json&clean=1',
          'sourceUrl': 'https://covid.cdc.gov/covid-data-tracker/#cases_casesinlast7days',
          'lastUpdatedSource': '2021-01-28T00:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        },
        {
          'infected': 1560,
          'tested': 'NA',
          'recovered': 1430,
          'deceased': 35,
          'country': 'Vietnam',
          'moreData': 'https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true',
          'historyData': 'https://api.apify.com/v2/datasets/RnzK2Aea1RlgBcauw/items?format=json&clean=1',
          'sourceUrl': 'https://ncov.moh.gov.vn/',
          'lastUpdatedSource': '2021-01-28T11:00:00.000Z',
          'lastUpdatedApify': '2021-01-28T20:00:00.000Z'
        }
      ]
    }
  },
  created () {
    this.gdata = this.processadata(this.globaldata_inc)
    this.casos = this.processadata_casos(this.globaldata_inc)
    this.recuperados = this.processadata_recuperados(this.globaldata_inc)
  },
  methods: {
    processadata (array) {
      const gdata_aux = []
      for (const i in array) {
        gdata_aux.push([array[i].country, array[i].deceased])
      }
      gdata_aux.sort(function (a, b) { return parseFloat(b[1]) - parseFloat(a[1]) })
      return gdata_aux
    },
    processadata_casos (array) {
      const gdata_aux = []
      for (const i in array) {
        gdata_aux.push([array[i].country, array[i].infected])
      }
      gdata_aux.sort(function (a, b) { return parseFloat(b[1]) - parseFloat(a[1]) })
      return gdata_aux
    },
    processadata_recuperados (array) {
      const recuperados_aux = []
      for (const i in array) {
        recuperados_aux.push([array[i].country, array[i].recovered])
      }
      recuperados_aux.sort(function (a, b) { return parseFloat(b[1]) - parseFloat(a[1]) })
      return recuperados_aux
    }
  }
}
</script>

<style>
.map1 {
  width: 1800px;
  box-sizing: border-box;
}
</style>
