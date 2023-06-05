import datetime
import os
from functools import reduce
import logging

import matplotlib.pyplot as plt
from django.db.models import Count
from django.db.models.functions import TruncDate
from .models import Sale, Medicine


logger = logging.getLogger('main')


def plot_last_days_sales():
    # Get the last three days' sales
    three_days_ago = datetime.datetime.today() - datetime.timedelta(days=3)
    logger.debug(f'three days ago - {three_days_ago}')
    sales = Sale.objects.filter(date__gte=three_days_ago.date())
    logger.debug(sales)

    # Calculate the sales count for each day
    daily_sales = sales.annotate(sale_date=TruncDate('date')).values('sale_date').annotate(sales_count=Count('id'))
    logger.debug(f'daily sales - {daily_sales}')

    # Get the most popular medicine
    medicine_count = {}
    for sale in sales:
        for medicine in sale.medicines.all():
            medicine_name = medicine.name
            medicine_count[medicine_name] = medicine_count.get(medicine_name, 0) + 1

    most_popular_medicine = max(medicine_count, key=medicine_count.get)

    # Prepare the data for plotting
    dates = [sale['sale_date'] for sale in daily_sales]
    logger.debug(f'{len(dates)}')
    for date in dates:
        logger.debug(f'{date}')
    sales_counts = [sale['sales_count'] for sale in daily_sales]

    # Create the plots
    plt.figure(figsize=(10, 5))

    # Plot for the most popular medicine
    plt.subplot(1, 2, 1)
    plt.bar(list(medicine_count.keys()), list(medicine_count.values()))
    plt.xlabel('Medicine')
    plt.ylabel('Count')
    plt.title('Most Popular Medicine')

    # Plot for the sales count for the last three days
    plt.subplot(1, 2, 2)
    plt.plot(dates, sales_counts, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Sales Count')
    plt.title('Last Three Days Sales Count')

    # Format the x-axis date labels
    plt.xticks(dates, [date.strftime('%Y-%m-%d') for date in dates])

    # Save the plot to a temporary file
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/pharmacy/images')
    plot_file = os.path.join(static_folder, 'plot.png')
    plt.savefig(plot_file)

