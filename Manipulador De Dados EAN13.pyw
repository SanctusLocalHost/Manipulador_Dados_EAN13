import os
import re
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter
from collections import Counter

# Dicionários de substituição
substituicoes_ean_para_nx = {
    "7898740470008,1": "NX 028-ABRAC",
    "7898740470015,1": "NX 001",
    "7898740470022,1": "NX 002",
    "7898740470039,1": "NX 003",
    "7898740470046,1": "NX 004",
    "7898740470053,1": "NX 005",
    "7898740470060,1": "NX 006",
    "7898740470077,1": "NX 007",
    "7898740470084,1": "NX 008",
    "7898740470091,1": "NX 009",
    "7898740470107,1": "NX 010",
    "7898740470114,1": "NX 011",
    "7898740470121,1": "NX 012",
    "7898740470138,1": "NX 013",
    "7898740470145,1": "NX 014",
    "7898740470152,1": "NX 015",
    "7898740470169,1": "NX 016",
    "7898740470176,1": "NX 017",
    "7898740470183,1": "NX 018",
    "7898740470190,1": "NX 019",
    "7898740470206,1": "NX 020",
    "7898740470213,1": "NX 021",
    "7898740470220,1": "NX 022",
    "7898740470237,1": "NX 023",
    "7898740470244,1": "NX 024",
    "7898740470251,1": "NX 025",
    "7898740470268,1": "NX 026",
    "7898740470275,1": "NX 027",
    "7898740470282,1": "NX 028",
    "7898740470299,1": "NX 029",
    "7898740470305,1": "NX 030",
    "7898740470312,1": "NX 031",
    "7898740470329,1": "NX 032",
    "7898740470336,1": "NX 033",
    "7898740470343,1": "NX 034",
    "7898740470350,1": "NX 035",
    "7898740470367,1": "NX 036",
    "7898740470374,1": "NX 037",
    "7898740470381,1": "NX 038",
    "7898740470398,1": "NX 039",
    "7898740470404,1": "NX 040",
    "7898740470411,1": "NX 041",
    "7898740470428,1": "NX 042",
    "7898740470435,1": "NX 043",
    "7898740470442,1": "NX 044",
    "7898740470459,1": "NX 045",
    "7898740470466,1": "NX 046",
    "7898740470473,1": "NX 047",
    "7898740470480,1": "NX 048",
    "7898740470497,1": "NX 049",
    "7898740470503,1": "NX 050",
    "7898740470510,1": "NX 051",
    "7898740470527,1": "NX 052",
    "7898740470534,1": "NX 053",
    "7898740470541,1": "NX 054",
    "7898740470558,1": "NX 055",
    "7898740470565,1": "NX 056",
    "7898740470572,1": "NX 057",
    "7898740470589,1": "NX 058",
    "7898740470596,1": "NX 059",
    "7898740470602,1": "NX 060",
    "7898740470619,1": "NX 061",
    "7898740470626,1": "NX 062",
    "7898740470633,1": "NX 063",
    "7898740470640,1": "NX 064",
    "7898740470657,1": "NX 065",
    "7898740470664,1": "NX 066",
    "7898740470671,1": "NX 067",
    "7898740470688,1": "NX 068",
    "7898740470695,1": "NX 069",
    "7898740470701,1": "NX 070",
    "7898740470718,1": "NX 071",
    "7898740470725,1": "NX 072",
    "7898740470732,1": "NX 073",
    "7898740470749,1": "NX 074",
    "7898740470756,1": "NX 075",
    "7898740470763,1": "NX 076",
    "7898740470770,1": "NX 077",
    "7898740470787,1": "NX 078",
    "7898740470794,1": "NX 079",
    "7898740470800,1": "NX 080",
    "7898740470817,1": "NX 081",
    "7898740470824,1": "NX 082",
    "7898740470831,1": "NX 083",
    "7898740470848,1": "NX 084",
    "7898740470855,1": "NX 085",
    "7898740470862,1": "NX 086",
    "7898740470879,1": "NX 087",
    "7898740470886,1": "NX 088",
    "7898740470893,1": "NX 089",
    "7898740470909,1": "NX 090",
    "7898740470916,1": "NX 091",
    "7898740470923,1": "NX 092",
    "7898740470930,1": "NX 093",
    "7898740470947,1": "NX 094",
    "7898740470954,1": "NX 095",
    "7898740470961,1": "NX 096",
    "7898740470978,1": "NX 097",
    "7898740470985,1": "NX 098",
    "7898740470992,1": "NX 099",
    "7898740471005,1": "NX 100",
    "7898740471012,1": "NX 101",
    "7898740471029,1": "NX 102",
    "7898740471036,1": "NX 103",
    "7898740471043,1": "NX 104",
    "7898740471050,1": "NX 105",
    "7898740471067,1": "NX 106",
    "7898740471074,1": "NX 107",
    "7898740471081,1": "NX 108",
    "7898740471098,1": "NX 109",
    "7898740471104,1": "NX 110",
    "7898740471111,1": "NX 111",
    "7898740471128,1": "NX 112",
    "7898740471135,1": "NX 113",
    "7898740471142,1": "NX 114",
    "7898740471159,1": "NX 115",
    "7898740471166,1": "NX 116",
    "7898740471173,1": "NX 117",
    "7898740471180,1": "NX 118",
    "7898740471197,1": "NX 119",
    "7898740471203,1": "NX 120",
    "7898740471210,1": "NX 121",
    "7898740471227,1": "NX 122",
    "7898740471234,1": "NX 123",
    "7898740471241,1": "NX 124",
    "7898740471258,1": "NX 125",
    "7898740471265,1": "NX 126",
    "7898740471272,1": "NX 127",
    "7898740471289,1": "NX 128",
    "7898740471296,1": "NX 129",
    "7898740471302,1": "NX 130",
    "7898740471319,1": "NX 131",
    "7898740471326,1": "NX 132",
    "7898740471333,1": "NX 133",
    "7898740471340,1": "NX 134",
    "7898740471357,1": "NX 135",
    "7898740471364,1": "NX 136",
    "7898740471371,1": "NX 137",
    "7898740471388,1": "NX 138",
    "7898740471395,1": "NX 139",
    "7898740471401,1": "NX 140",
    "7898740471418,1": "NX 141",
    "7898740471425,1": "NX 142",
    "7898740471432,1": "NX 143",
    "7898740471449,1": "NX 144",
    "7898740471456,1": "NX 145",
    "7898740471463,1": "NX 146",
    "7898740471470,1": "NX 147",
    "7898740471487,1": "NX 148",
    "7898740471494,1": "NX 149",
    "7898740471500,1": "NX 150",
    "7898740471517,1": "NX 151",
    "7898740471524,1": "NX 152",
    "7898740471531,1": "NX 153",
    "7898740471548,1": "NX 154",
    "7898740471555,1": "NX 155",
    "7898740471562,1": "NX 156",
    "7898740471579,1": "NX 157",
    "7898740471586,1": "NX 158",
    "7898740471593,1": "NX 159",
    "7898740471609,1": "NX 160",
    "7898740471616,1": "NX 161",
    "7898740471623,1": "NX 162",
    "7898740471630,1": "NX 163",
    "7898740471647,1": "NX 164",
    "7898740471654,1": "NX 165",
    "7898740471661,1": "NX 166",
    "7898740471678,1": "NX 167",
    "7898740471685,1": "NX 168",
    "7898740471692,1": "NX 169",
    "7898740471708,1": "NX 170",
    "7898740471715,1": "NX 171",
    "7898740471722,1": "NX 172",
    "7898740471739,1": "NX 173",
    "7898740471746,1": "NX 174",
    "7898740471753,1": "NX 175",
    "7898740471760,1": "NX 176",
    "7898740471777,1": "NX 177",
    "7898740471784,1": "NX 178",
    "7898740471791,1": "NX 179",
    "7898740471807,1": "NX 180",
    "7898740471814,1": "NX 181",
    "7898740471821,1": "NX 182",
    "7898740471838,1": "NX 183",
    "7898740471845,1": "NX 184",
    "7898740471852,1": "NX 185",
    "7898740471869,1": "NX 186",
    "7898740471876,1": "NX 187",
    "7898740471883,1": "NX 188",
    "7898740471890,1": "NX 189",
    "7898740471906,1": "NX 190",
    "7898740471913,1": "NX 191",
    "7898740471920,1": "NX 192",
    "7898740471937,1": "NX 193",
    "7898740471944,1": "NX 194",
    "7898740471951,1": "NX 195",
    "7898740471968,1": "NX 196",
    "7898740471975,1": "NX 197",
    "7898740471982,1": "NX 198",
    "7898740471999,1": "NX 199",
    "7898740472002,1": "NX 200",
    "7898740472019,1": "NX 201",
    "7898740472026,1": "NX 202",
    "7898740472033,1": "NX 203",
    "7898740472040,1": "NX 204",
    "7898740472057,1": "NX 205",
    "7898740472064,1": "NX 206",
    "7898740472071,1": "NX 207",
    "7898740472088,1": "NX 208",
    "7898740472095,1": "NX 209",
    "7898740472101,1": "NX 210",
    "7898740472118,1": "NX 211",
    "7898740472125,1": "NX 212",
    "7898740472132,1": "NX 213",
    "7898740472149,1": "NX 214",
    "7898740472156,1": "NX 215",
    "7898740472163,1": "NX 216",
    "7898740472170,1": "NX 217",
    "7898740472187,1": "NX 218",
    "7898740472194,1": "NX 219",
    "7898740472200,1": "NX 220",
    "7898740472217,1": "NX 221",
    "7898740472224,1": "NX 222",
    "7898740472231,1": "NX 223",
    "7898740472248,1": "NX 224",
    "7898740472255,1": "NX 225",
    "7898740472262,1": "NX 226",
    "7898740472279,1": "NX 227",
    "7898740472286,1": "NX 228",
    "7898740472293,1": "NX 229",
    "7898740472309,1": "NX 230",
    "7898740472316,1": "NX 231",
    "7898740472323,1": "NX 232",
    "7898740472330,1": "NX 233",
    "7898740472347,1": "NX 234",
    "7898740472354,1": "NX 235",
    "7898740472361,1": "NX 236",
    "7898740472378,1": "NX 237",
    "7898740472385,1": "NX 238",
    "7898740472392,1": "NX 239",
    "7898740472408,1": "NX 240",
    "7898740472415,1": "NX 241",
    "7898740472422,1": "NX 242",
    "7898740472439,1": "NX 243",
    "7898740472446,1": "NX 244",
    "7898740472453,1": "NX 245",
    "7898740472460,1": "NX 246",
    "7898740472477,1": "NX 247",
    "7898740472484,1": "NX 248",
    "7898740472491,1": "NX 249",
    "7898740472507,1": "NX 250",
    "7898740472514,1": "NX 251",
    "7898740472521,1": "NX 252",
    "7898740472538,1": "NX 253",
	"7898740472545,1": "NX 254",
	"7894325102432,1": "523402",
    "7894325103644,1": "523437",
    "7894325000110,1": "526033",
    "7894325000271,1": "526034",
    "7894325000264,1": "526036",
    "7894325008147,1": "526044",
    "7894325000943,1": "526048",
    "7894325002510,1": "526055",
    "7894325003258,1": "526059",
    "7894325004156,1": "526065",
    "7894325002848,1": "526198",
    "7894325004071,1": "526199",
    "7894325004064,1": "526200",
    "7894325000066,1": "526201",
    "7894325002183,1": "526202",
    "7894325000059,1": "526203",
    "7894325008499,1": "526205",
    "7894325001667,1": "526206",
    "7894325001247,1": "526211",
    "7894325003968,1": "526212",
    "7894325001650,1": "526291",
    "7894325001674,1": "526292",
    "7894325003777,1": "526294",
    "7894325000837,1": "526297",
    "7894325002138,1": "526388",
    "7894325002565,1": "526389",
    "7894325001513,1": "526391",
    "7894325004514,1": "526392",
    "7894325001940,1": "526393",
    "7894325003241,1": "526399",
    "7894325001940,1": "526488",
    "7894325100001,1": "526489",
    "7894325001261,1": "526502",
    "7894325001605,1": "526503",
    "7894325003807,1": "526504",
    "7894325004606,1": "526505",
    "7894325001728,1": "526506",
    "7894325001438,1": "526507",
    "7894325002206,1": "526508",
    "7894325004163,1": "526509",
    "7894325004972,1": "526511",
    "7894325000295,1": "526538",
    "7894325001285,1": "526539",
    "7894325004989,1": "526540",
    "7894325002435,1": "526541",
    "7894325005276,1": "526542",
    "7894325100988,1": "523391D",
    "7894325100988,1": "523391E",
}


substituicoes_nx_para_ean = {v.replace(" ", "").lower(): k for k, v in substituicoes_ean_para_nx.items()}


def get_most_common_prefix(files):
    if not files:
        return None

    # Encontra o prefixo mais longo comum entre os arquivos
    prefix = os.path.commonprefix(files)
    # Remove qualquer parte do prefixo que inclua um ponto (.) para evitar cortar no meio de extensões
    prefix = prefix.split('.')[0]
    return prefix


def add_final_newline(filepath):
    # Certifica-se de que o arquivo termine com uma nova linha
    with open(filepath, 'a') as file:
        file.write('\n')


def concatenate_files(directory):
    exclude_extensions = ['.exe', '.py', '.pyw', '.jpg', '.jpeg', '.png', '.xls', '.xlsx']
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))
             and not any(file.endswith(ext) for ext in exclude_extensions)]

    most_common_prefix = get_most_common_prefix(files)
    if not most_common_prefix:
        most_common_prefix = "OUTFILE"
    output_filename = f"{most_common_prefix}_AGRUPADO.txt"
    output_filepath = os.path.join(directory, output_filename)

    linha_em_branco = "\n"

    with open(output_filepath, 'w') as outfile:
        for i, file in enumerate(files):
            with open(os.path.join(directory, file), 'r') as infile:
                for line in infile:
                    if line.strip():
                        outfile.write(line)
            if i < len(files) - 1:
                outfile.write(linha_em_branco)

    add_final_newline(output_filepath)

    folder_name = output_filename.replace('.txt', '')
    output_folder_path = os.path.join(directory, folder_name)
    os.makedirs(output_folder_path, exist_ok=True)
    os.replace(output_filepath, os.path.join(output_folder_path, output_filename))

    print(f"Arquivos concatenados e pasta '{folder_name}' criada com sucesso em '{output_folder_path}'!")


def converter_arquivos(substituicoes, add_spaces=False):
    diretorio = os.path.dirname(os.path.abspath(__file__))

    nova_pasta = os.path.join(diretorio, "BIPAGEM CONVERTIDA")
    os.makedirs(nova_pasta, exist_ok=True)

    exclude_extensions = ['.py', '.pyw', '.exe', '.jpg', '.jpeg', '.png', '.xls', '.xlsx']

    for filename in os.listdir(diretorio):
        if not any(filename.endswith(ext) for ext in exclude_extensions):
            file_path = os.path.join(diretorio, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                for antigo, novo in substituicoes.items():
                    if add_spaces:
                        parts = novo.split(',')
                        if len(parts) >= 2:
                            novo = parts[0] + ' ' * (9 - len(parts[0])) + ',' + parts[1]
                    content = content.replace(antigo, novo)

                novo_nome = filename + "_CONVERTIDO"
                novo_arquivo_path = os.path.join(nova_pasta, novo_nome)
                with open(novo_arquivo_path, "w", encoding="utf-8") as novo_arquivo:
                    novo_arquivo.write(content)

    messagebox.showinfo("Sucesso", "BIPAGENS CONVERTIDAS COM SUCESSO!!!")


def converter_ean_para_nx():
    converter_arquivos(substituicoes_ean_para_nx, add_spaces=True)


def converter_nx_para_ean():
    converter_arquivos(substituicoes_nx_para_ean)


def buscar_termo():
    termo = entry_termo.get().strip()
    if not termo:
        messagebox.showwarning("Aviso", "Por favor, insira um termo para buscar.")
        return

    resultados_text.delete(1.0, tk.END)

    ignore_ext = ('.py', '.pyw', '.exe', '.jpg', '.jpeg', '.png', '.xlsx', '.xls')

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    arquivos = [f for f in os.listdir(diretorio_atual) if
                os.path.isfile(os.path.join(diretorio_atual, f)) and not f.endswith(ignore_ext)]
    encontrados = []

    for arquivo in arquivos:
        try:
            with open(os.path.join(diretorio_atual, arquivo), 'r', encoding='utf-8') as f:
                conteudo = f.read()
                if termo.lower() in conteudo.lower():
                    encontrados.append(arquivo)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")

    if encontrados:
        resultados_text.insert(tk.END, f"Itens localizados nos seguintes arquivos:\n")
        for arquivo in encontrados:
            resultados_text.insert(tk.END, f"- {arquivo}\n")
    else:
        resultados_text.insert(tk.END, "Nenhum item encontrado.")


def buscar(event=None):
    entrada = entry.get().replace(" ", "").lower()
    if entrada in substituicoes_ean_para_nx:
        resultado = substituicoes_ean_para_nx[entrada]
        ean_image = generate_ean13_barcode(resultado.split(',')[0])
        resultado_label.config(text=resultado, font=("Arial", 12, "bold"))
        ean_label.config(image=ean_image)
        ean_label.image = ean_image
        copy_button.config(state=tk.NORMAL)
    elif entrada in substituicoes_nx_para_ean:
        resultado = substituicoes_nx_para_ean[entrada]
        ean_image = generate_ean13_barcode(resultado.split(',')[0])
        resultado_label.config(text=resultado, font=("Arial", 12, "bold"))
        ean_label.config(image=ean_image)
        ean_label.image = ean_image
        copy_button.config(state=tk.NORMAL)
    else:
        resultado = "Peça ou EAN não encontrado."
        resultado_label.config(text=resultado, font=("Arial", 12, "bold"))
        ean_label.config(image=None)
        copy_button.config(state=tk.DISABLED)


def copiar():
    resultado = resultado_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(resultado)


def generate_ean13_barcode(ean):
    ean = barcode.get_barcode_class('ean13')(ean, writer=ImageWriter())
    barcode_image = ean.render()
    return ImageTk.PhotoImage(barcode_image)


root = tk.Tk()
root.title("Ferramentas de Verificação - Sua Empresa V1.8 STABLE")

# Estilo para as abas do notebook
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Arial", 10, "bold"), padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", "lightblue")])

# Estilo para os botões
style.configure("TButton", font=("Arial", 10), padding=5)

# Estilo para entradas de texto
entry_style = ttk.Style()
entry_style.configure("TEntry", font=("Arial", 10))

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Aba de conversão de EAN para NX e vice-versa
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="CONVERTER EAN NX")

btn_convert_ean_nx = ttk.Button(frame1, text="Converter EAN para NX", command=converter_ean_para_nx)
btn_convert_ean_nx.place(relx=0.5, rely=0.3, anchor='center')

btn_convert_nx_ean = ttk.Button(frame1, text="Converter NX para EAN", command=converter_nx_para_ean)
btn_convert_nx_ean.place(relx=0.5, rely=0.5, anchor='center')

hint_label_ean_nx = ttk.Label(frame1, text="Use esta área para Converter códigos EAN para NX e Vice-versa.",
                              font=("Arial", 8, "italic"))
hint_label_ean_nx.pack(side='bottom', pady=5)

# Aba de concatenação de arquivos
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="AGRUPAR BIPAGENS")

btn_concatenate = ttk.Button(frame2, text="AGRUPAR ARQUIVOS",
                             command=lambda: concatenate_files(os.path.dirname(os.path.abspath(__file__))))
btn_concatenate.place(relx=0.5, rely=0.4, anchor='center')

hint_label_concat = ttk.Label(frame2, text="Use esta área para Agrupar arquivos de Bipagens em um único arquivo.",
                              font=("Arial", 8, "italic"))
hint_label_concat.pack(side='bottom', pady=5)

# Aba de pesquisa EAN
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="PESQUISAR EAN")

entry_label = ttk.Label(frame3, text="Digite o nome da Peça ou EAN13:", font=("Arial", 10, "bold"))
entry_label.pack(pady=5)

entry = ttk.Entry(frame3, width=50, style="TEntry")
entry.pack(pady=5)
entry.bind("<Return>", buscar)
entry.bind("<KP_Enter>", buscar)

search_button = ttk.Button(frame3, text="Buscar", command=buscar)
search_button.pack(pady=5)

hint_label = ttk.Label(frame3, text="Exemplo: 7898740470053,1 ou NX 005", font=("Arial", 8, "italic"))
hint_label.pack(pady=5)

result_frame = ttk.Frame(frame3)
result_frame.pack(pady=10)

resultado_label = ttk.Label(result_frame, text="", wraplength=400, font=("Arial", 10))
resultado_label.pack(pady=5)

ean_label = ttk.Label(result_frame)
ean_label.pack(pady=10)

copy_button = ttk.Button(result_frame, text="Copiar Resultado", command=copiar, state=tk.DISABLED)
copy_button.pack(pady=5)

# Aba de localização de termos
frame4 = ttk.Frame(notebook)
notebook.add(frame4, text="LOCALIZAR ITENS")

entry_label = ttk.Label(frame4, text="Digite o item que deseja Localizar:", font=("Arial", 10, "bold"))
entry_label.pack(pady=5)

entry_termo = ttk.Entry(frame4, width=50, style="TEntry")
entry_termo.pack(pady=5)

btn_buscar = ttk.Button(frame4, text="Buscar", command=buscar_termo)
btn_buscar.pack(pady=5)

hint_label = ttk.Label(frame4, text="Área Especializada na Localização de itens em Bipagens... Digite Ex: 005", font=("Arial", 8, "italic"))
hint_label.pack(side='bottom', pady=5)

resultados_text = tk.Text(frame4, height=15, width=50, font=("Arial", 10))
resultados_text.pack(pady=10)

root.mainloop()
