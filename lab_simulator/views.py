import numpy as np
import matplotlib.pyplot as plt
import os
from django.conf import settings
from django.shortcuts import render

# Function to calculate projectile motion
def projectile_motion(velocity, angle):
    g = 9.8  # gravitational acceleration (m/s^2)
    angle_rad = np.radians(angle)  # convert angle to radians
    t_max = 2 * velocity * np.sin(angle_rad) / g  # time of flight
    t_steps = np.linspace(0, t_max, num=30)  # 30 time steps
    
    # Calculate x and y coordinates of the projectile at each time step
    x = velocity * np.cos(angle_rad) * t_steps  # x(t) = v0 * cos(θ) * t
    y = velocity * np.sin(angle_rad) * t_steps - 0.5 * g * t_steps**2  # y(t) = v0 * sin(θ) * t - 1/2 * g * t^2
    
    observations = list(zip(t_steps, x, y))  # combine time, x, and y values
    return observations, t_max

# View to handle the form and display the results
def projectile_view(request):
    if request.method == "POST":
        # Retrieve velocity and angle values from the form
        velocity = float(request.POST.get("velocity"))
        angle = float(request.POST.get("angle"))
        
        # Get observations and max time of flight
        observations, t_max = projectile_motion(velocity, angle)
        
        # Plotting the projectile motion
        fig, ax = plt.subplots()
        ax.plot([obs[1] for obs in observations], [obs[2] for obs in observations])
        ax.set_title("Projectile Motion")
        ax.set_xlabel("Distance (m)")
        ax.set_ylabel("Height (m)")
        ax.grid(True)
        
        # Save plot to the static directory
        plot_filename = 'virtual_lab.jpg'
        plot_path = os.path.join(settings.STATICFILES_DIRS[0], 'lab_simulator', 'images', plot_filename)  # Correct static file saving path
        plt.savefig(plot_path)
        plt.close()  # Close the plot to avoid memory issues

        # Pass observations, max time, and plot URL to the template
        plot_url = f"{settings.STATIC_URL}lab_simulator/images/{plot_filename}"  # Correct URL path for static files
        return render(request, "lab_simulator/simulator.html", {
            "observations": observations,
            "t_max": t_max,
            "velocity": velocity,
            "angle": angle,
            "plot_url": plot_url,  # Pass the URL of the plot
        })
    
    # Return the form template if the method is GET
    return render(request, "lab_simulator/simulator_form.html")
