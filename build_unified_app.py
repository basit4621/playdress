import sys
import os

sys.path.append('/home/gamp/.gemini/antigravity/scratch/play-dress-up-web')
from assets_b64 import (
    MODEL_HER_FASHION, MODEL_EMERALD, MODEL_NOIR, MODEL_ROSE, DOLL_2D,
    PROD_TOP, PROD_SKIRT, PROD_BOOTS, PROD_BAG, PROD_EMERALD, PROD_NOIR, PROD_ROSE
)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PLAY DRESS UP – Unified Store & Dressing Room</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');
    
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #E2E2E2;
    }}
    .font-serif {{
      font-family: 'Playfair Display', serif;
    }}
    
    /* Interactive Card Selected Style */
    .store-card {{
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .card-active-equipped {{
      border-color: #1c1917 !important;
      background-color: #FAFAFA !important;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
    }}
    
    /* Smooth model cross-fade */
    #center-model-img, #center-doll-img {{
      transition: opacity 0.3s ease-in-out, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    /* 360 Ring animation */
    @keyframes spin-slow {{
      from {{ transform: rotateX(65deg) rotateZ(0deg); }}
      to {{ transform: rotateX(65deg) rotateZ(360deg); }}
    }}
    .animate-spin-pedestal {{
      animation: spin-slow 20s linear infinite;
    }}
  </style>
</head>
<body class="text-stone-800 antialiased p-2 sm:p-4 md:p-6 min-h-screen flex items-center justify-center">

  <!-- ======================================================== -->
  <!-- MAIN STUDIO CONTAINER (HER FASHION 3-COLUMN UNIFIED LAYOUT) -->
  <!-- ======================================================== -->
  <div class="max-w-[1400px] w-full bg-[#EDEDED] p-3 sm:p-5 md:p-6 rounded-[36px] shadow-2xl border border-stone-300">

    <!-- TOP HEADER BAR -->
    <header class="flex flex-wrap items-center justify-between pb-3.5 mb-4 border-b border-stone-300/80 px-2 gap-3">
      
      <!-- Brand & Mode -->
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-2xl bg-stone-900 text-white flex items-center justify-center font-serif font-extrabold text-xl shadow-md">
          P
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg font-extrabold tracking-tight text-stone-900 font-serif">PLAY DRESS UP</h1>
            <span class="bg-stone-900 text-white text-[9px] font-black uppercase px-2 py-0.5 rounded-full tracking-wider">Studio</span>
          </div>
          <p class="text-[11px] font-semibold text-stone-500">Unified Dressing Room & Multi-Vendor Store</p>
        </div>
      </div>

      <!-- Avatar Mode Toggle: 3D Runway Model vs 2D Doll Avatar -->
      <div class="bg-white/80 backdrop-blur p-1 rounded-2xl border border-stone-200 flex items-center gap-1 shadow-sm">
        <button onclick="setAvatarMode('3d')" id="btn-mode-3d" class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm">
          <span>👠</span> 3D Fashion Model
        </button>
        <button onclick="setAvatarMode('2d')" id="btn-mode-2d" class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900">
          <span>🪞</span> 2D Doll Avatar
        </button>
      </div>

      <!-- Coins & User Balance -->
      <div class="flex items-center gap-3">
        <div class="bg-gradient-to-r from-amber-50 to-amber-100 border border-amber-300/80 text-amber-900 px-3.5 py-1.5 rounded-2xl text-xs font-bold flex items-center gap-2 shadow-sm">
          <span class="text-base">🪙</span>
          <div>
            <span class="font-extrabold">450 Coins</span>
            <span class="text-[10px] text-amber-700 block -mt-0.5 font-medium">$15.00 Voucher Active</span>
          </div>
        </div>
        
        <div class="w-9 h-9 rounded-full bg-stone-800 text-white flex items-center justify-center font-bold text-xs ring-2 ring-white shadow">
          O
        </div>
      </div>

    </header>

    <!-- ======================================================== -->
    <!-- 3-COLUMN UNIFIED GRID: Left Store | Center Avatar | Right Look -->
    <!-- ======================================================== -->
    <div class="grid grid-cols-1 lg:grid-cols-10 gap-4 md:gap-5 items-stretch">

      <!-- ======================================================== -->
      <!-- COLUMN 1 (LEFT, 3.5 cols): STORE CATALOG (HER FASHION)   -->
      <!-- ======================================================== -->
      <div class="lg:col-span-4 bg-white p-4 sm:p-5 rounded-[32px] shadow-sm border border-stone-200 flex flex-col justify-between">
        
        <div>
          <!-- Store Selector & Header -->
          <div class="flex items-center justify-between pb-3 border-b border-stone-100 mb-3.5">
            <div>
              <span class="text-[10px] font-bold text-stone-400 uppercase tracking-widest block">Shop by Store</span>
              <div class="flex items-center gap-1.5 cursor-pointer group">
                <h2 id="store-brand-title" class="text-base font-extrabold text-stone-900 font-serif tracking-tight">HER FASHION</h2>
                <span class="text-xs text-stone-400 group-hover:text-stone-800 transition">▾</span>
              </div>
            </div>
            
            <div class="flex items-center gap-1.5">
              <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 border border-emerald-200 text-[10px] font-bold px-2 py-0.5 rounded-full">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Verified Vendor
              </span>
            </div>
          </div>

          <!-- Search Bar -->
          <div class="relative mb-3.5">
            <span class="absolute inset-y-0 left-3 flex items-center text-stone-400 text-xs">🔍</span>
            <input type="text" placeholder="Search dresses, tops, boots, bags..." class="w-full pl-8 pr-3 py-2 bg-stone-50 border border-stone-200 rounded-xl text-xs font-medium text-stone-800 focus:bg-white focus:outline-none focus:ring-1 focus:ring-stone-400 transition placeholder:text-stone-400">
          </div>

          <!-- Curated Outfit Looks Selector -->
          <div class="mb-3.5">
            <span class="text-[10px] font-extrabold text-stone-400 uppercase tracking-wider block mb-1.5">Curated Complete Looks (Tap to Style Avatar)</span>
            <div class="grid grid-cols-2 gap-1.5">
              <button onclick="selectOutfitLook('minimalist')" id="btn-look-minimalist" class="look-btn p-2 rounded-xl text-left border border-stone-900 bg-stone-900 text-white text-[11px] font-bold transition flex items-center justify-between">
                <span>✨ Look 1: Neutral Luxe</span>
                <span class="text-[9px] opacity-75">$558</span>
              </button>
              <button onclick="selectOutfitLook('emerald')" id="btn-look-emerald" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-emerald-50 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                <span>💚 Look 2: Emerald Silk</span>
                <span class="text-[9px] text-emerald-700">$89</span>
              </button>
              <button onclick="selectOutfitLook('noir')" id="btn-look-noir" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-stone-100 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                <span>🖤 Look 3: Velvet Noir</span>
                <span class="text-[9px] text-stone-600">$119</span>
              </button>
              <button onclick="selectOutfitLook('rose')" id="btn-look-rose" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-rose-50 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                <span>🌸 Look 4: Rose Satin</span>
                <span class="text-[9px] text-rose-600">$79</span>
              </button>
            </div>
          </div>

          <!-- Category Filter Pills -->
          <div class="flex items-center gap-1.5 overflow-x-auto pb-1 mb-3.5 text-[11px] font-semibold text-stone-600 scrollbar-none">
            <button onclick="filterCategory('all')" class="cat-pill px-3 py-1 bg-stone-900 text-white rounded-full font-bold">All</button>
            <button onclick="filterCategory('tops')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Tops</button>
            <button onclick="filterCategory('skirts')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Skirts</button>
            <button onclick="filterCategory('dresses')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Dresses</button>
            <button onclick="filterCategory('shoes')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Shoes</button>
            <button onclick="filterCategory('bags')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Bags</button>
          </div>

          <!-- 2-COLUMN PRODUCT GRID (EXACT TO HER FASHION) -->
          <div class="grid grid-cols-2 gap-3 max-h-[380px] overflow-y-auto pr-1">

            <!-- Card 1: Off-Shoulder Top -->
            <div onclick="toggleSingleItem('top')" id="card-top" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_TOP}" alt="Off-shoulder Top" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">ZARA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$29.90</span>
                  <span id="badge-top" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                </div>
              </div>
            </div>

            <!-- Card 2: Pleated Maxi Skirt -->
            <div onclick="toggleSingleItem('skirt')" id="card-skirt" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_SKIRT}" alt="Pleated Maxi Skirt" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">MANGO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$49.99</span>
                  <span id="badge-skirt" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                </div>
              </div>
            </div>

            <!-- Card 3: Knee-High Leather Boots -->
            <div onclick="toggleSingleItem('boots')" id="card-boots" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_BOOTS}" alt="Leather Boots" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">BERSHKA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Knee-high leather boots</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$129.00</span>
                  <span id="badge-boots" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                </div>
              </div>
            </div>

            <!-- Card 4: Tabby Shoulder Bag -->
            <div onclick="toggleSingleItem('bag')" id="card-bag" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_BAG}" alt="Tabby Shoulder Bag" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">COACH</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$350.00</span>
                  <span id="badge-bag" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                </div>
              </div>
            </div>

            <!-- Card 5: Emerald Silk Wrap Maxi Dress (Direct from User Request!) -->
            <div onclick="selectOutfitLook('emerald')" id="card-emerald" class="store-card cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-emerald-50/50 rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_EMERALD}" alt="Emerald Silk Wrap Maxi" class="h-full object-contain drop-shadow">
              </div>
              <div>
                <span class="text-[9px] font-bold text-emerald-700 uppercase tracking-wider">ZARA COLLECTION</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Emerald silk wrap maxi</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$89.00</span>
                  <span id="badge-emerald" class="text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded">Tap to Wear</span>
                </div>
              </div>
            </div>

            <!-- Card 6: Velvet Noir Slip Gown -->
            <div onclick="selectOutfitLook('noir')" id="card-noir" class="store-card cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
              <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
              <div class="w-full h-24 bg-stone-100/70 rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                <img src="{PROD_NOIR}" alt="Noir Velvet Gown" class="h-full object-contain drop-shadow">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">MANGO STUDIO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Noir velvet slip gown</h4>
                <div class="flex items-center justify-between mt-1">
                  <span class="text-xs font-extrabold text-stone-900">$119.00</span>
                  <span id="badge-noir" class="text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded">Tap to Wear</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Vendor Delivery Guarantee Badge -->
        <div class="mt-3.5 pt-3 border-t border-stone-100 flex items-center justify-between text-[11px] text-stone-500">
          <span class="flex items-center gap-1.5">
            <span>📦</span> Doorstep delivery in 2-4 days
          </span>
          <span class="font-bold text-stone-700">100% Authentic</span>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- COLUMN 2 (CENTER, 3.5 cols): DRESSING ROOM (TRANSPARENT) -->
      <!-- ======================================================== -->
      <div class="lg:col-span-3 bg-[#E9E9E9] rounded-[32px] p-4 flex flex-col justify-between items-center relative overflow-hidden border border-stone-300 shadow-inner min-h-[580px]">
        
        <!-- Top Floating Status Pill -->
        <div class="w-full flex items-center justify-between z-20">
          <span class="bg-white/90 backdrop-blur-md px-3 py-1 rounded-full text-[10px] font-bold text-stone-700 border border-stone-200/80 shadow-sm flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span id="center-tag-text">Look 1 • Neutral Luxe</span>
          </span>

          <span class="bg-stone-900/80 text-white text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm">
            Live Preview
          </span>
        </div>

        <!-- Left Stack Mini Floating Product Preview (Identical to HER FASHION inspo_3) -->
        <div class="absolute left-4 top-16 z-20 flex flex-col gap-2" id="floating-mini-stack">
          <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-top">
            <img src="{PROD_TOP}" class="h-full object-contain">
          </div>
          <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-skirt">
            <img src="{PROD_SKIRT}" class="h-full object-contain">
          </div>
          <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-boots">
            <img src="{PROD_BOOTS}" class="h-full object-contain">
          </div>
          <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-bag">
            <img src="{PROD_BAG}" class="h-full object-contain">
          </div>
        </div>

        <!-- ===================================================== -->
        <!-- THE MODEL IN THE CENTER (100% TRANSPARENT CUTOUT)     -->
        <!-- NO BACKGROUND AT ALL! SITS CLEANLY ON THE 3D PEDESTAL -->
        <!-- ===================================================== -->
        <div class="relative w-full h-[470px] flex flex-col items-center justify-end z-10">
          
          <!-- MODEL CONTAINER -->
          <div class="relative w-[240px] h-[450px] flex items-end justify-center">
            
            <!-- 1. 3D Runway Fashion Model (100% Clean Cutout) -->
            <img 
              id="center-model-img" 
              src="{MODEL_HER_FASHION}" 
              alt="3D Fashion Model" 
              class="h-full object-contain select-none drop-shadow-xl z-10"
              style="display: block;"
            >

            <!-- 2. 2D Doll Avatar (100% Clean Cutout with Bun) -->
            <img 
              id="center-doll-img" 
              src="{DOLL_2D}" 
              alt="2D Doll Avatar" 
              class="h-full object-contain select-none drop-shadow-xl z-10"
              style="display: none;"
            >

          </div>

          <!-- 3D CIRCULAR PEDESTAL & 360 ROTATION RING -->
          <div class="absolute bottom-[-10px] w-[210px] h-[55px] flex items-center justify-center pointer-events-none">
            <!-- Platform Cylinder -->
            <div class="w-full h-full bg-gradient-to-b from-stone-100 to-stone-300 rounded-[100%] shadow-lg border border-stone-300/80"></div>
            <!-- Concentric Pedestal Step -->
            <div class="absolute w-[80%] h-[75%] bg-gradient-to-b from-white to-stone-200 rounded-[100%] shadow-inner border border-stone-200"></div>
            <!-- Circular 360° Indicator Ring -->
            <div class="absolute w-[95%] h-[90%] border-2 border-dashed border-stone-400/60 rounded-[100%] animate-spin-pedestal flex items-center justify-center"></div>
            <span class="absolute bottom-1 bg-stone-800 text-white text-[9px] font-black px-2 py-0.5 rounded-full shadow-sm z-20">
              360°
            </span>
          </div>

        </div>

        <!-- Bottom Current Status Pill -->
        <div class="w-full flex justify-center z-20 mt-1">
          <span class="bg-white/95 backdrop-blur-md px-4 py-1.5 rounded-full border border-stone-200 text-xs font-bold text-stone-800 shadow-sm flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span id="equipped-summary-text">Wearing: Zara Top + Mango Skirt + Leather Boots + Coach Bag</span>
          </span>
        </div>

      </div>

      <!-- ======================================================== -->
      <!-- COLUMN 3 (RIGHT, 2.5 cols): "YOUR LOOK" SUMMARY          -->
      <!-- ======================================================== -->
      <div class="lg:col-span-3 bg-white p-4 sm:p-5 rounded-[32px] shadow-sm border border-stone-200 flex flex-col justify-between">
        
        <div>
          <!-- Header -->
          <div class="border-b border-stone-100 pb-3 mb-3.5 px-1 flex items-center justify-between">
            <h3 class="text-xs font-extrabold text-stone-800 uppercase tracking-widest">YOUR LOOK</h3>
            <span id="outfit-tag-badge" class="text-[9px] font-extrabold uppercase px-2 py-0.5 bg-stone-100 text-stone-600 rounded-md">Curated Look</span>
          </div>

          <!-- Equipped Items Stack -->
          <div class="space-y-2 mb-4 max-h-[220px] overflow-y-auto pr-1" id="your-look-items-list">
            
            <!-- Item 1: Off-shoulder top -->
            <div id="row-top" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                  <img src="{PROD_TOP}" class="h-full object-contain">
                </div>
                <div>
                  <span class="text-[9px] font-bold text-stone-400 uppercase">ZARA</span>
                  <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                  <p class="text-xs font-extrabold text-stone-900 mt-0.5">$29.90</p>
                </div>
              </div>
              <span class="text-stone-400 text-xs font-bold">›</span>
            </div>

            <!-- Item 2: Pleated maxi skirt -->
            <div id="row-skirt" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                  <img src="{PROD_SKIRT}" class="h-full object-contain">
                </div>
                <div>
                  <span class="text-[9px] font-bold text-stone-400 uppercase">MANGO</span>
                  <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                  <p class="text-xs font-extrabold text-stone-900 mt-0.5">$49.99</p>
                </div>
              </div>
              <span class="text-stone-400 text-xs font-bold">›</span>
            </div>

            <!-- Item 3: Knee-high leather boots -->
            <div id="row-boots" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                  <img src="{PROD_BOOTS}" class="h-full object-contain">
                </div>
                <div>
                  <span class="text-[9px] font-bold text-stone-400 uppercase">BERSHKA</span>
                  <h4 class="text-xs font-bold text-stone-900 leading-tight">Leather boots</h4>
                  <p class="text-xs font-extrabold text-stone-900 mt-0.5">$129.00</p>
                </div>
              </div>
              <span class="text-stone-400 text-xs font-bold">›</span>
            </div>

            <!-- Item 4: Tabby Shoulder Bag -->
            <div id="row-bag" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                  <img src="{PROD_BAG}" class="h-full object-contain">
                </div>
                <div>
                  <span class="text-[9px] font-bold text-stone-400 uppercase">COACH</span>
                  <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                  <p class="text-xs font-extrabold text-stone-900 mt-0.5">$350.00</p>
                </div>
              </div>
              <span class="text-stone-400 text-xs font-bold">›</span>
            </div>

          </div>

          <!-- STYLE & FIT FEEDBACK (Identical to HER FASHION inspo_3) -->
          <div class="mb-4 p-3.5 bg-stone-50 rounded-2xl border border-stone-200/80 space-y-2 text-xs text-stone-600">
            <h4 class="text-[10px] font-extrabold uppercase tracking-wider text-stone-500">STYLE & FIT</h4>
            <div class="space-y-1.5 text-[11px]">
              <p class="flex items-center justify-between font-semibold text-stone-700">
                <span class="flex items-center gap-1.5">
                  <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                  <span id="fit-size-text">Fits your size (Bust 34", Waist 26")</span>
                </span>
                <span class="text-stone-400 text-[10px]">ⓘ</span>
              </p>
              <p class="flex items-center justify-between font-semibold text-stone-700">
                <span class="flex items-center gap-1.5">
                  <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                  <span id="fit-color-text">Color harmony: Warm Taupe & Cream</span>
                </span>
                <span class="text-stone-400 text-[10px]">ⓘ</span>
              </p>
              <p class="flex items-center justify-between font-semibold text-stone-700">
                <span class="flex items-center gap-1.5">
                  <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                  <span id="fit-occasion-text">Occasion: Evening Casual</span>
                </span>
                <span class="text-stone-400 text-[10px]">ⓘ</span>
              </p>
            </div>
          </div>

        </div>

        <!-- PRICING BREAKDOWN & CHECKOUT (WITH COINS REWARD APPLIED) -->
        <div class="border-t border-stone-100 pt-3 space-y-2.5">
          
          <div class="space-y-1.5 text-xs text-stone-600">
            <div class="flex items-center justify-between font-medium">
              <span>Subtotal</span>
              <span id="subtotal-val" class="font-bold text-stone-800">$558.89</span>
            </div>
            
            <div class="flex items-center justify-between font-medium text-emerald-700 bg-emerald-50 px-2 py-1 rounded-lg">
              <span class="flex items-center gap-1">
                <span>🪙</span> Coins Discount (150 Coins)
              </span>
              <span class="font-bold">-$15.00</span>
            </div>
            
            <div class="flex items-center justify-between font-medium text-stone-500">
              <span>Doorstep Delivery</span>
              <span class="text-stone-800 font-bold">FREE</span>
            </div>
            
            <div class="flex items-center justify-between text-base font-extrabold text-stone-900 border-t border-stone-200/80 pt-1.5">
              <span>Total</span>
              <span id="total-val">$543.89</span>
            </div>
          </div>

          <!-- Checkout Button -->
          <button onclick="openCheckoutModal()" class="w-full py-3 px-4 bg-stone-900 hover:bg-black text-white rounded-2xl font-bold text-xs uppercase tracking-wider shadow-lg hover:shadow-xl transition flex items-center justify-center gap-2 group">
            <span>Shop the Look</span>
            <span class="group-hover:translate-x-0.5 transition">→</span>
          </button>

          <p class="text-[10px] text-center text-stone-400">Secure delivery to your doorstep • 30-day free return</p>

        </div>

      </div>

    </div>

  </div>

  <!-- CHECKOUT MODAL -->
  <div id="checkout-modal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white max-w-md w-full rounded-[32px] p-6 shadow-2xl border border-stone-200 text-stone-800 animate-in fade-in zoom-in-95 duration-200">
      <div class="flex items-center justify-between pb-3 border-b border-stone-100">
        <h3 class="font-serif font-bold text-lg text-stone-900">Doorstep Order Summary</h3>
        <button onclick="closeCheckoutModal()" class="w-7 h-7 rounded-full bg-stone-100 text-stone-500 hover:text-stone-800 font-bold text-sm">✕</button>
      </div>

      <div class="py-4 space-y-3">
        <div class="bg-stone-50 p-3.5 rounded-2xl border border-stone-200">
          <p class="text-xs font-bold text-stone-800 mb-1">Delivering to:</p>
          <p class="text-xs text-stone-600">Oreoluwa • Victoria Island, Lagos / London</p>
          <p class="text-[11px] text-emerald-700 font-semibold mt-1">✓ Estimated delivery: 2-3 business days</p>
        </div>

        <div class="flex justify-between items-center text-sm font-extrabold text-stone-900 py-1">
          <span>Amount Payable:</span>
          <span id="modal-total-val" class="text-lg text-stone-900">$543.89</span>
        </div>

        <div class="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900">
          🪙 <strong>150 Play Dress Up Coins redeemed!</strong> You earned +45 coins for this purchase.
        </div>
      </div>

      <div class="space-y-2">
        <button onclick="confirmOrder()" class="w-full py-3 bg-stone-900 hover:bg-black text-white rounded-2xl font-bold text-xs uppercase tracking-wider transition">
          Confirm & Pay Doorstep Delivery
        </button>
        <button onclick="closeCheckoutModal()" class="w-full py-2.5 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-2xl font-bold text-xs transition">
          Continue Styling
        </button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT FOR DYNAMIC DRESS UP & INTERACTION -->
  <script>
    // Asset base64 URLs
    const ASSETS = {{
      model_minimalist: "{MODEL_HER_FASHION}",
      model_emerald: "{MODEL_EMERALD}",
      model_noir: "{MODEL_NOIR}",
      model_rose: "{MODEL_ROSE}",
      doll_2d: "{DOLL_2D}",
      prod_top: "{PROD_TOP}",
      prod_skirt: "{PROD_SKIRT}",
      prod_boots: "{PROD_BOOTS}",
      prod_bag: "{PROD_BAG}",
      prod_emerald: "{PROD_EMERALD}",
      prod_noir: "{PROD_NOIR}",
      prod_rose: "{PROD_ROSE}"
    }};

    // Active Outfit State
    let currentLook = 'minimalist';
    let avatarMode = '3d'; // '3d' or '2d'

    // Individual item toggles for minimalist look
    const itemState = {{
      top: true,
      skirt: true,
      boots: true,
      bag: true
    }};

    const prices = {{
      top: 29.90,
      skirt: 49.99,
      boots: 129.00,
      bag: 350.00
    }};

    // Switch Avatar Mode: 3D Runway Model vs 2D Doll Avatar
    function setAvatarMode(mode) {{
      avatarMode = mode;
      const modelImg = document.getElementById('center-model-img');
      const dollImg = document.getElementById('center-doll-img');
      const btn3d = document.getElementById('btn-mode-3d');
      const btn2d = document.getElementById('btn-mode-2d');

      if (mode === '3d') {{
        modelImg.style.display = 'block';
        dollImg.style.display = 'none';
        btn3d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm';
        btn2d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900';
      }} else {{
        modelImg.style.display = 'none';
        dollImg.style.display = 'block';
        btn2d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm';
        btn3d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900';
      }}
    }}

    // Select curated outfit look (Minimalist, Emerald, Noir, Rose)
    function selectOutfitLook(lookKey) {{
      currentLook = lookKey;
      const modelImg = document.getElementById('center-model-img');
      const tagText = document.getElementById('center-tag-text');
      const summaryText = document.getElementById('equipped-summary-text');
      const storeBrand = document.getElementById('store-brand-title');
      const lookBadge = document.getElementById('outfit-tag-badge');
      const itemsList = document.getElementById('your-look-items-list');

      // Update Look buttons styling
      document.querySelectorAll('.look-btn').forEach(btn => {{
        btn.classList.remove('bg-stone-900', 'text-white', 'border-stone-900');
        btn.classList.add('bg-stone-50', 'text-stone-800', 'border-stone-200');
      }});
      const activeBtn = document.getElementById('btn-look-' + lookKey);
      if (activeBtn) {{
        activeBtn.classList.add('bg-stone-900', 'text-white', 'border-stone-900');
        activeBtn.classList.remove('bg-stone-50', 'text-stone-800', 'border-stone-200');
      }}

      if (lookKey === 'minimalist') {{
        modelImg.src = ASSETS.model_minimalist;
        tagText.innerText = 'Look 1 • Neutral Luxe';
        summaryText.innerText = 'Wearing: Zara Top + Mango Skirt + Leather Boots + Coach Bag';
        storeBrand.innerText = 'HER FASHION';
        lookBadge.innerText = 'Curated 4-Piece Look';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Warm Taupe & Cream';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Evening Casual / Art Gallery';

        // Restore 4-item list
        itemsList.innerHTML = `
          <div id="row-top" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_top}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">ZARA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$29.90</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-skirt" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_skirt}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">MANGO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$49.99</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-boots" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_boots}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">BERSHKA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Leather boots</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$129.00</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-bag" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_bag}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">COACH</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$350.00</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
        `;

        updateTotals(558.89);
        updateCardBadges('minimalist');

      }} else if (lookKey === 'emerald') {{
        modelImg.src = ASSETS.model_emerald;
        tagText.innerText = 'Look 2 • Emerald Silk Maxi';
        summaryText.innerText = 'Wearing: Zara Emerald Silk Wrap Maxi Dress';
        storeBrand.innerText = 'ZARA FLAGSHIP';
        lookBadge.innerText = 'Runway Silk Collection';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Deep Jewel Emerald Green';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Gala / Cocktail Soirée';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-emerald-50/70 rounded-2xl border border-emerald-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-emerald-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_emerald}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-emerald-700 uppercase">ZARA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Emerald silk wrap maxi</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$89.00</p>
              </div>
            </div>
            <span class="text-emerald-600 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(89.00);
        updateCardBadges('emerald');

      }} else if (lookKey === 'noir') {{
        modelImg.src = ASSETS.model_noir;
        tagText.innerText = 'Look 3 • Noir Velvet';
        summaryText.innerText = 'Wearing: Mango Noir Velvet Slip Gown';
        storeBrand.innerText = 'MANGO STUDIO';
        lookBadge.innerText = 'Evening Capsule';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Midnight Black Velvet';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Black Tie Event';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-stone-100 rounded-2xl border border-stone-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_noir}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-500 uppercase">MANGO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Noir velvet slip gown</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$119.00</p>
              </div>
            </div>
            <span class="text-stone-800 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(119.00);
        updateCardBadges('noir');

      }} else if (lookKey === 'rose') {{
        modelImg.src = ASSETS.model_rose;
        tagText.innerText = 'Look 4 • Rose Quartz';
        summaryText.innerText = 'Wearing: Rose Quartz Satin Wrap Dress';
        storeBrand.innerText = 'H&M PREMIUM';
        lookBadge.innerText = 'Summer Soirée';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Blush Pink & Pearl';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Afternoon Tea / Date Night';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-rose-50 rounded-2xl border border-rose-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-rose-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_rose}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-rose-500 uppercase">H&M</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Rose quartz satin dress</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$79.00</p>
              </div>
            </div>
            <span class="text-rose-500 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(79.00);
        updateCardBadges('rose');
      }}
    }}

    // Update badges on product cards
    function updateCardBadges(lookKey) {{
      const cards = ['top', 'skirt', 'boots', 'bag', 'emerald', 'noir'];
      cards.forEach(k => {{
        const card = document.getElementById('card-' + k);
        const badge = document.getElementById('badge-' + k);
        if (card && badge) {{
          if (lookKey === 'minimalist' && ['top', 'skirt', 'boots', 'bag'].includes(k)) {{
            card.classList.add('card-active-equipped');
            badge.innerText = 'Equipped ✓';
            badge.className = 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded';
          }} else if (k === lookKey) {{
            card.classList.add('card-active-equipped');
            badge.innerText = 'Equipped ✓';
            badge.className = 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded';
          }} else {{
            card.classList.remove('card-active-equipped');
            badge.innerText = 'Tap to Add';
            badge.className = 'text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded';
          }}
        }}
      }});
    }}

    // Toggle single item on minimalist look
    function toggleSingleItem(key) {{
      if (currentLook !== 'minimalist') {{
        selectOutfitLook('minimalist');
        return;
      }}

      itemState[key] = !itemState[key];
      const isEquipped = itemState[key];

      const card = document.getElementById('card-' + key);
      const badge = document.getElementById('badge-' + key);
      const row = document.getElementById('row-' + key);
      const mini = document.getElementById('mini-' + key);

      if (card) {{
        if (isEquipped) card.classList.add('card-active-equipped');
        else card.classList.remove('card-active-equipped');
      }}
      if (badge) {{
        badge.innerText = isEquipped ? 'Equipped ✓' : 'Tap to Add';
        badge.className = isEquipped 
          ? 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded'
          : 'text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded';
      }}
      if (row) row.style.opacity = isEquipped ? '1' : '0.3';
      if (mini) mini.style.opacity = isEquipped ? '1' : '0.2';

      // Recalculate
      let sub = 0;
      const equipped = [];
      if (itemState.top) {{ sub += prices.top; equipped.push('Zara Top'); }}
      if (itemState.skirt) {{ sub += prices.skirt; equipped.push('Mango Skirt'); }}
      if (itemState.boots) {{ sub += prices.boots; equipped.push('Leather Boots'); }}
      if (itemState.bag) {{ sub += prices.bag; equipped.push('Coach Bag'); }}

      document.getElementById('equipped-summary-text').innerText = equipped.length > 0
        ? 'Wearing: ' + equipped.join(' + ')
        : 'Avatar in underlayer • Tap items to dress up';

      updateTotals(sub);
    }}

    function updateTotals(subtotal) {{
      const subtotalEl = document.getElementById('subtotal-val');
      const totalEl = document.getElementById('total-val');
      const modalTotal = document.getElementById('modal-total-val');

      const discount = subtotal > 15 ? 15.00 : 0;
      const total = Math.max(0, subtotal - discount);

      subtotalEl.innerText = '$' + subtotal.toFixed(2);
      totalEl.innerText = '$' + total.toFixed(2);
      if (modalTotal) modalTotal.innerText = '$' + total.toFixed(2);
    }}

    function filterCategory(cat) {{
      document.querySelectorAll('.cat-pill').forEach(btn => {{
        btn.classList.remove('bg-stone-900', 'text-white');
        btn.classList.add('bg-stone-100', 'text-stone-700');
      }});
      event.target.classList.add('bg-stone-900', 'text-white');
      event.target.classList.remove('bg-stone-100', 'text-stone-700');
    }}

    function toggleFav(btn) {{
      btn.classList.toggle('text-red-500');
      btn.innerText = btn.classList.contains('text-red-500') ? '♥' : '♡';
    }}

    function openCheckoutModal() {{
      document.getElementById('checkout-modal').classList.remove('hidden');
    }}

    function closeCheckoutModal() {{
      document.getElementById('checkout-modal').classList.add('hidden');
    }}

    function confirmOrder() {{
      alert('🎉 Order Confirmed! Your curated outfit is being prepared for doorstep delivery to your address. 150 Coins applied as discount!');
      closeCheckoutModal();
    }}
  </script>
</body>
</html>
"""

# Write out to index.html and blueprint.html
target_index = '/home/gamp/.gemini/antigravity/scratch/play-dress-up-web/index.html'
target_blueprint = '/home/gamp/.gemini/antigravity/scratch/play-dress-up-web/blueprint.html'
artifact_path = '/home/gamp/.gemini/antigravity/brain/5988c679-a518-4b3a-a908-6a809de30903/visual_design_blueprints.html'

with open(target_index, 'w') as f:
    f.write(html_template)

with open(target_blueprint, 'w') as f:
    f.write(html_template)

with open(artifact_path, 'w') as f:
    f.write(html_template)

print("Unified store and dressing room successfully built across all targets!")
