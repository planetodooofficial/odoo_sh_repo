# -*- coding: utf-8 -*-
from odoo import api, models, fields, _


class ProductSpecification(models.Model):
    _inherit = 'product.template'

    ps_origin_name = fields.Char('Origin')
    ps_botanical_name = fields.Char('Botanical Name')
    ps_harmonization_code = fields.Char('Harmonization Code')
    ps_packaging = fields.Char('Packaging')
    ps_pallet_qty = fields.Char('Full Pallet Qty')
    ps_storage = fields.Char('Storage')
    ps_shelf_life = fields.Char('Shelf life')
    ps_accreditations = fields.Char('Accreditations')

    # Characteristics

    ps_appearance = fields.Char('Appearance')
    ps_odour = fields.Char('Odour')
    ps_flavour = fields.Char('Flavour')
    ps_texture = fields.Char('Texture')
    ps_purity = fields.Char('Purity')
    ps_mesh_size = fields.Char('Mesh Size')
    ps_broken_pieces = fields.Char('Broken Pieces')
    ps_foreign_material = fields.Char('Foreign material')

    # Mycotoxins

    ps_aflotoxin_b1 = fields.char('Aflotoxin B1')
    ps_aflotoxin_b2 = fields.char('Aflotoxin B2')
    ps_aflotoxin_g1 = fields.char('Aflotoxin G1')
    ps_aflotoxin_g2 = fields.char('Aflotoxin G2')
    ps_ochratoxin_a = fields.char('Ochratoxin A')

    # PAH

    ps_naphthalene = fields.Char('Naphthalene')
    ps_acenaphthylene = fields.Char('Acenaphthylene')
    ps_acenaphthene = fields.Char('Acenaphthene')
    ps_fluorene = fields.Char('Fluorene')
    ps_phenanthrene = fields.Char('Phenanthrene')
    ps_fluoranthene = fields.Char('Fluoranthene')
    ps_benz_a_anthracene = fields.Char('Benz(a)anthracene')
    ps_anthracene = fields.Char('Anthracene')
    ps_Benz_b_fluoranthene = fields.Char('Benz(b)fluoranthene')
    ps_chrysene = fields.Char('Chrysene')
    ps_Benz_a_pyrene = fields.Char('Benz(a)pyrene')
    ps_Benz_k_fluoranthene = fields.Char('Benz(k)fluoranthene')
    ps_Benz_g_h_i_pyrene = fields.Char('Benz(g.h.i)pyrene')
    ps_Dibenz_a_h_anthracene = fields.Char('Dibenz(a.h)anthracene')
    ps_pyrene = fields.Char('Pyrene')
    ps_indenk_1_2_3_c_d_pyrene = fields.Char('Indenk(1.2.3-c.d)pyrene')
    ps_sum_PAH_4 = fields.Char('Sum PAH 4')

    # Heavy Metals

    ps_pb = fields.Char('Pb')
    ps_hg = fields.Char('Hg')
    ps_as = fields.Char('As')
    ps_cd = fields.Char('Cd')

    # Fatty Acids

    ps_palmitic = fields.Char('Palmitic Acid')
    ps_myristic = fields.Char('Myristic Acid')
    ps_margaric = fields.Char('Margaric Acid')
    ps_palmitoleic = fields.Char('Palmitoleic Acid')
    ps_oleic = fields.Char('Oleic Acid')
    ps_stearic = fields.Char('Stearic Acid')
    ps_alpha_linoleic = fields.Char('Alpha Linoleic Acid')
    ps_linoleic = fields.Char('Linoleic Acid')
    ps_stearidonic = fields.Char('Stearidonic Acid')
    ps_gamma_linoleic = fields.Char('Gamma linoleic Acid')
    ps_eicosenoic_Acid = fields.Char('Eicosenoic Acid')
    ps_arachidic = fields.Char('Arachidic Acid')
    ps_behenic = fields.Char('Behenic Acid')
    ps_eicosadienoic = fields.Char('Eicosadienoic Acid')
    ps_sterols = fields.Char('Sterols')
    ps_arachidonic = fields.Char('Arachidonic Acid')

    # Amino Acid

    ps_alanine = fields.Char('Alanine')
    ps_arginine = fields.Char('Arginine')
    ps_aspartic_acid = fields.Char('Aspartic Acid')
    ps_cysteine = fields.Char('Cysteine')
    ps_glutamic_acid = fields.Char('Glutamic Acid')
    ps_glycine = fields.Char('Glycine')
    ps_histidine = fields.Char('Histidine')
    ps_isoleucine = fields.Char('Isoleucine')
    ps_leucine = fields.Char('Leucine')
    ps_lysine = fields.Char('Lysine')
    ps_methionine = fields.Char('Methionine')
    ps_phenylalanine = fields.Char('Phenylalanine')
    ps_proline = fields.Char('Proline')
    ps_serine = fields.Char('Serine')
    ps_threonine = fields.Char('Threonine')
    ps_tryptophan = fields.Char('Tryptophan')
    ps_tyrosine = fields.Char('Tyrosine')
    ps_valine = fields.Char('Valine')

    # Nutritional Values

    ps_energy = fields.Char('Energy')
    ps_fat = fields.Char('Fat')
    ps_saturated = fields.Char('Saturated')
    ps_p_unsaturated = fields.Char('Poly Unsaturated')
    ps_m_unsaturated = fields.Char('Mono Unsaturated')
    ps_t_unsaturated = fields.Char('Total Unsaturated')
    ps_omega_3 = fields.Char('Omega 3')
    ps_omega_6 = fields.Char('Omega 6')
    ps_omega_9 = fields.Char('Omega 9')
    ps_trans_fatty_acids = fields.Char('Trans fatty acids')
    ps_carbohydrates = fields.Char('Carbohydrates')
    ps_sugar = fields.Char('Sugars total')
    ps_sucrose = fields.Char('Sucrose')
    ps_fructose = fields.Char('Fructose')
    ps_glucose = fields.Char('Glucose')
    ps_maltose = fields.Char('Maltose')
    ps_dietary_fiber_total = fields.Char('Dietary Fiber Total')
    ps_protein = fields.Char('Protein')
    ps_salt = fields.Char('Salt')

    # Vitamins

    ps_vitamin_a = fields.Char('Vitamin A')
    ps_vitamin_b1 = fields.Char('Vitamin B1')
    ps_vitamin_b2 = fields.Char('Vitamin B2')
    ps_vitamin_b3 = fields.Char('Vitamin B3')
    ps_vitamin_b4 = fields.Char('Vitamin B4')
    ps_vitamin_b5 = fields.Char('Vitamin B5')
    ps_vitamin_b6 = fields.Char('Vitamin B6')
    ps_vitamin_b7 = fields.Char('Vitamin B7')
    ps_vitamin_b8 = fields.Char('Vitamin B8')
    ps_vitamin_b9 = fields.Char('Vitamin B9')
    ps_vitamin_b12 = fields.Char('Vitamin B12')
    ps_vitamin_b15 = fields.Char('Vitamin B15')
    ps_vitamin_b17 = fields.Char('Vitamin B17')
    ps_vitamin_c = fields.Char('Vitamin C')
    ps_vitamin_d = fields.Char('Vitamin D')
    ps_vitamin_d2 = fields.Char('Vitamin D2')
    ps_vitamin_d3 = fields.Char('Vitamin D3')
    ps_vitamin_e = fields.Char('Vitamin E')

    # Minerals

    ps_calcium = fields.Char('Calcium')
    ps_chromium = fields.Char('Chromium')
    ps_copper = fields.Char('Copper')
    ps_iodine = fields.Char('Iodine')
    ps_iron = fields.Char('Iron')
    ps_manganese = fields.Char('Manganese')
    ps_molybdenum = fields.Char('Molybdenum')
    ps_phosphorus = fields.Char('Phosphorus')
    ps_potassium = fields.Char('Potassium')
    ps_selenium = fields.Char('Selenium')
    ps_sodium = fields.Char('Sodium')
    ps_zinc = fields.Char('Zinc')
    ps_magnesium = fields.Char('Magnesium')

    # Microbiology

    ps_aerobic_plate_count = fields.Char('Aerobic Plate Count')
    ps_yeast = fields.Char('Yeast')
    ps_moulds = fields.Char('Moulds')
    ps_enterobacteriaceae = fields.Char('Enterobacteriaceae')
    ps_salmonella = fields.Char('Salmonella')
    ps_escherichia_coli = fields.Char('Escherichia Coli')
    ps_coliforms = fields.Char('Coliforms')
    ps_staphylococcus_aureus = fields.Char('Staphylococcus Aureus')
    ps_bacillus_cereus = fields.Char('Bacillus Cereus')
    ps_free_fatty_acid = fields.Char('Free Fatty Acid')
    ps_acid_value = fields.Char('Acid Value')
    ps_peroxide = fields.Char('Peroxide number')
    ps_thc = fields.Char('THC')
    ps_moisture = fields.Char('Moisture')
    ps_chlorophyll = fields.Char('Chlorophyll')
    ps_sulphur_dioxide = fields.Char('Sulphur Dioxide(SO2)')
    ps_ash = fields.Char('Ash')
    ps_cholesterol = fields.Char('Cholesterol')
    ps_carotenoid = fields.Char('Carotenoid')
    ps_ph = fields.Char('PH value')
    ps_caffein = fields.Char('Caffein')

    # Statements

    ps_undesirable_substances = fields.Char('Undesirable substances')
    ps_animal_testing = fields.Char('Undesirable substances')
    ps_pesticides = fields.Char('Pesticides')
    ps_irradiation = fields.Char('Irradiation')
    ps_gmo = fields.Char('GMO Free')

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



