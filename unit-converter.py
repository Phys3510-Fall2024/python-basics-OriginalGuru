# Conversion factors and inverse relationship flag
# more comments
conversion_factors = {
    ("THz", "ps"): (1, True),                # Linear Frequency to Period (inverse; T=1/f)
    ("ps", "THz"): (1, True),                # Period to Linear Frequency (inverse; f=1/T)
    ("THz", "cm-1"): (33.356, False),        # Linear Frequency to Linear Wavenumber (k = f/c)
    ("THz", "meV"): (4.1357, False),         # linear frequency to energy in meV (E=hf, h is Planck's constant)
    ("THz", "cm"): (0.03, True)              # linear frequency to wavelength in cm (lambda = c/f, c is the speed of light)
}

# Example of how to access the dictionary
# Let's say we want to convert from THz to ps
conversion_key = ("THz", "cm")

if conversion_key in conversion_factors:
    factor, is_inverse = conversion_factors[conversion_key]
    print(f"Conversion factor: {factor}")
    print(f"Is inverse relationship: {is_inverse}")
else:
    print("Conversion not supported.")
