# Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes.

class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    price = "$8.99"
    num_devices = 1

class StandardPlan(BasicPlan):
    price = "$12.99"
    num_devices = 2
    has_HD = True
    has_UHD = False

class PremiumPlan(BasicPlan):
    price = "$15.99"
    num_devices = 4
    has_HD = True
    has_UHD = True

BasicPlan = BasicPlan()
print(f"BASIC PLAN - Can stream: {BasicPlan.can_stream}")
print(f"BASIC PLAN - Can download: {BasicPlan.can_download}")
print(f"BASIC PLAN - Has SD: {BasicPlan.has_SD}")
print(f"BASIC PLAN - Has HD: {BasicPlan.has_HD}")
print(f"BASIC PLAN - Has UHD: {BasicPlan.has_UHD}")
print(f"BASIC PLAN - Number of devices: {BasicPlan.num_devices}")
print(f"BASIC PLAN - Price: {BasicPlan.price}")

StandardPlan = StandardPlan()
print(f"STANDARD PLAN - Can stream: {StandardPlan.can_stream}")
print(f"STANDARD PLAN - Can download: {StandardPlan.can_download}")
print(f"STANDARD PLAN - Has SD: {StandardPlan.has_SD}")
print(f"STANDARD PLAN - Has HD: {StandardPlan.has_HD}")
print(f"STANDARD PLAN - Has UHD: {StandardPlan.has_UHD}")
print(f"STANDARD PLAN - Number of devices: {StandardPlan.num_devices}")
print(f"STANDARD PLAN - Price: {StandardPlan.price}")

PremiumPlan = PremiumPlan()
print(f"PREMIUM PLAN - Can stream: {PremiumPlan.can_stream}")
print(f"PREMIUM PLAN - Can download: {PremiumPlan.can_download}")
print(f"PREMIUM PLAN - Has SD: {PremiumPlan.has_SD}")
print(f"PREMIUM PLAN - Has HD: {PremiumPlan.has_HD}")
print(f"PREMIUM PLAN - Has UHD: {PremiumPlan.has_UHD}")
print(f"PREMIUM PLAN - Number of devices: {PremiumPlan.num_devices}")
print(f"PREMIUM PLAN - Price: {PremiumPlan.price}")

