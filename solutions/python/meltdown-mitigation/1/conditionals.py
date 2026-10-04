"""Functions to prevent a nuclear meltdown."""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    # Semua 3 kondisi harus terpenuhi (True)
    return (temperature < 800) and \
           (neutrons_emitted > 500) and \
           ((temperature * neutrons_emitted) < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    # Hitung persentase efisiensi
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    # Kelompokkan berdasarkan persentase
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    # Hitung nilai temperature * neutrons per second
    power_output = temperature * neutrons_produced_per_second
    
    # Tentukan batas 90% dan 110% dari threshold
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold
    
    # Cek kondisi
    if power_output < lower_bound:
        return 'LOW'
    elif lower_bound <= power_output <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'