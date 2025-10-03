import psutil
import datetime

output_file = "diagnostico_ec2.txt"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')
net_io = psutil.net_io_counters()
processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:5]

with open(output_file, "w") as f:
    f.write(f"Relatório de Diagnóstico - {timestamp}\n")
    f.write("="*50 + "\n\n")

    f.write("🔧 CPU\n")
    f.write(f"Uso de CPU: {cpu_percent}%\n\n")

    f.write("🧠 Memória\n")
    f.write(f"Total: {memory.total / (1024**3):.2f} GB\n")
    f.write(f"Usada: {memory.used / (1024**3):.2f} GB\n")
    f.write(f"Disponível: {memory.available / (1024**3):.2f} GB\n")
    f.write(f"Uso: {memory.percent}%\n\n")

    f.write("💾 Disco (/)\n")
    f.write(f"Total: {disk.total / (1024**3):.2f} GB\n")
    f.write(f"Usado: {disk.used / (1024**3):.2f} GB\n")
    f.write(f"Disponível: {disk.free / (1024**3):.2f} GB\n")
    f.write(f"Uso: {disk.percent}%\n\n")

    f.write("🌐 Rede\n")
    f.write(f"Bytes enviados: {net_io.bytes_sent / (1024**2):.2f} MB\n")
    f.write(f"Bytes recebidos: {net_io.bytes_recv / (1024**2):.2f} MB\n\n")

    f.write("📊 Processos com maior uso de CPU\n")
    for proc in processes:
        info = proc.info
        f.write(f"PID: {info['pid']}, Nome: {info['name']}, CPU: {info['cpu_percent']}%, Memória: {info['memory_percent']:.2f}%\n")

print(f"Relatório salvo em {output_file}")
