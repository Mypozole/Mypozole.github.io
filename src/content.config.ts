import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Eight records, per MyPozole_Design_System.md section 4 and
// MyPozole_Claude_Design_Build_Brief.md section 2. Every page reads from
// these instead of being hand-built, so growth means adding rows.

const products = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/products' }),
  schema: z.object({
    protein: z.enum(['pork', 'chicken', 'vegan']),
    style: z.enum(['white', 'red', 'green']),
    format: z.enum(['32oz pouch', '16oz cup']),
    price: z.number().nullable(),
    priceSource: z.string().nullable(),
    sku: z.string().nullable(),
    ingredients: z.array(z.string()).nullable(),
    allergens: z.array(z.string()).nullable(),
    nutrition: z.object({
      servingSize: z.string(),
      calories: z.number(),
      fatGrams: z.number(),
      cholesterolMg: z.number(),
      sodiumMg: z.number(),
      carbGrams: z.number(),
      fiberGrams: z.number(),
      sugarGrams: z.number(),
      proteinGrams: z.number(),
    }),
    labelFormatIssue: z.string().nullable(),
  }),
});

const locations = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/locations' }),
  schema: z.object({
    name: z.string(),
    type: z.enum(['store', 'market', 'truck-stop']),
    city: z.string(),
    address: z.string().nullable(),
    mapsLink: z.string().nullable(),
    source: z.string(),
  }),
});

const stock = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/stock' }),
  schema: z.object({
    locationId: z.string(),
    carries: z.array(z.string()), // product ids, e.g. "pork-white"
    source: z.string(),
  }),
});

const menuItems = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/menu-items' }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    longDescription: z.string(),
    fulfillment: z.enum(['delivery-or-pickup', 'market-and-trailer-only']),
    fulfillmentNote: z.string(),
    order: z.number(),
  }),
});

const toppings = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/toppings' }),
  schema: z.object({
    name: z.string(),
    included: z.boolean(),
    extraPrice: z.number().nullable(),
    source: z.string(),
  }),
});

const stories = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/stories' }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    body: z.string().nullable(),
    status: z.enum(['ready', 'needs-sourcing']),
    sourceNote: z.string().nullable(),
  }),
});

const testimonials = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/testimonials' }),
  schema: z.object({
    quote: z.string(),
    source: z.string(),
    context: z.string().nullable(),
  }),
});

const wholesaleStats = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/wholesale-stats' }),
  schema: z.object({
    label: z.string(),
    value: z.string(),
    source: z.string(),
  }),
});

export const collections = {
  products,
  locations,
  stock,
  menuItems,
  toppings,
  stories,
  testimonials,
  wholesaleStats,
};
