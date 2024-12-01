{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing\n",
    "data_panen = {  \n",
    "    'lokasi1': {\n",
    "        'nama_lokasi': 'Kebun A',\n",
    "        'hasil_panen': {\n",
    "            'padi': 1200,\n",
    "            'jagung': 800,\n",
    "            'kedelai': 500\n",
    "        }\n",
    "    },\n",
    "    'lokasi2': {\n",
    "        'nama_lokasi': 'Kebun B',\n",
    "        'hasil_panen': {\n",
    "            'padi': 1500,\n",
    "            'jagung': 900,\n",
    "            'kedelai': 450\n",
    "        }\n",
    "    },\n",
    "    'lokasi3': {\n",
    "        'nama_lokasi': 'Kebun C',\n",
    "        'hasil_panen': {\n",
    "            'padi': 1100,\n",
    "            'jagung': 750,\n",
    "            'kedelai': 600\n",
    "        }\n",
    "    },\n",
    "    'lokasi4': {\n",
    "        'nama_lokasi': 'Kebun D',\n",
    "        'hasil_panen': {\n",
    "            'padi': 1300,\n",
    "            'jagung': 850,\n",
    "            'kedelai': 550\n",
    "        }\n",
    "    },\n",
    "    'lokasi5': {\n",
    "        'nama_lokasi': 'Kebun E',\n",
    "        'hasil_panen': {\n",
    "            'padi': 1400,\n",
    "            'jagung': 950,\n",
    "            'kedelai': 480\n",
    "        }\n",
    "    }\n",
    "}\n",
    "\n",
    "for key, value in data_panen.items():\n",
    "    print(f\"Hasil panen {value['nama_lokasi']}:\")\n",
    "    print(f\"Padi: {value['hasil_panen']['padi']}\")\n",
    "    print(f\"Jagung: {value['hasil_panen']['jagung']}\")\n",
    "    print(f\"Kedelai: {value['hasil_panen']['kedelai']}\\n\")"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
