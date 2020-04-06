# -*- coding: utf-8 -*-
from odoo import api, models, fields, _


class ProductSpecification(models.Model):
    _inherit = 'product.template'

    ps_product_name = fields.Char('Name')
    ps_botanical_name = fields.Char('Botanical Name')
    ps_euterpe_precatoria = fields.Char('Euterpe Precatoria')
    ps_harmonization_code = fields.Char('Harmonization Code')
    ps_packaging = fields.Char('Packaging')
    ps_storage = fields.Char('Storage')
    ps_shelf_life = fields.Char('Shelf life')
    ps_accreditations = fields.Char('Accreditations')

    # Characteristics

    ps_appearance = fields.Char('Appearance')
    ps_odour = fields.Char('Odour')
    ps_texture = fields.Char('Texture')
    ps_foreign_material = fields.Char('Foreign Material')

    # Nutritional Values

    ps_energy = fields.Char('Energy')
    ps_fat = fields.Char('Fat')
    ps_saturated = fields.Char('Saturated')
    ps_unsaturated = fields.Char('Unsaturated')
    ps_trans_fatty_acids = fields.Char('Trans fatty acids')
    ps_carbohydrates = fields.Char('Carbohydrates')
    ps_dietary_fiber_total = fields.Char('Dietary Fiber Total')
    ps_protein = fields.Char('Protein')
    ps_salt = fields.Char('Salt')

    # Vitamins

    ps_vitamin = fields.Char('Vitamin C')

    # Minerals

    ps_calcium = fields.Char('Calcium')
    ps_iron = fields.Char('Iron')
    ps_phosphorus = fields.Char('Phosphorus')
    ps_potassium = fields.Char('Potassium')
    ps_sodium = fields.Char('Sodium')
    ps_magnesium = fields.Char('Magnesium')

    # Microbiology

    ps_aerobic_plate_count = fields.Char('Aerobic Plate Count')
    ps_yeast = fields.Char('Yeast')
    ps_moulds = fields.Char('Moulds')
    ps_salmonella = fields.Char('Salmonella')
    ps_escherichia_coli = fields.Char('Escherichia Coli')
    ps_coliforms = fields.Char('Coliforms')
    ps_staphylococcus_aureus = fields.Char('Staphylococcus Aureus')
    ps_moisture = fields.Char('Moisture')

    # Allergens

    ps_cereals_containing_gluten = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Cereals Containing Gluten')
    ps_crustaceans_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Crustaceans and products thereof')
    ps_eggs_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Eggs and products thereof')
    ps_fish_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Fish and products thereof')
    ps_peanuts_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Peanuts and products thereof')
    ps_soybeans_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Soybeans and products thereof')
    ps_milk_products_thereof_including_lactose = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Milk and products thereof including lactose')
    ps_nuts = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Nuts i.e. almonds')
    ps_celery_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Celery and products thereof')
    ps_mustard_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Mustard and products thereof')
    ps_sesame_seeds_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Sesame seeds and products thereof')
    ps_sulphur_dioxide_sulphites = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Sulphur dioxide and sulphites')
    ps_lupin_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Lupin and products thereof')
    ps_molluscs_products_thereof = fields.Selection([('yes', 'YES'), ('no', 'NO')], string='Molluscs and products thereof')



