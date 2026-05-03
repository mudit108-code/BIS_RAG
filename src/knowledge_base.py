"""
BIS Standards Knowledge Base - SP 21 Building Materials
Covers: Cement, Steel, Concrete, Aggregates, Bricks, Pipes, Roofing, etc.
"""

BIS_STANDARDS = [
    # ─── CEMENT ───────────────────────────────────────────────────────────────
    {
        "id": "IS 269: 1989",
        "title": "Specification for Ordinary Portland Cement, 33 Grade",
        "category": "Cement",
        "keywords": [
            "ordinary portland cement", "opc", "33 grade", "33grade",
            "cement chemical requirements", "cement physical requirements",
            "general construction cement", "portland cement manufacturing",
            "small enterprise cement", "mse cement"
        ],
        "description": (
            "Covers chemical composition, physical properties, and testing "
            "requirements for 33 Grade Ordinary Portland Cement (OPC). "
            "Applicable for general construction, masonry, plaster, and "
            "non-structural uses. Specifies limits on compounds like C3S, "
            "C2S, alumina, iron oxide, magnesia, and sulfate content. "
            "Also covers setting time, soundness, compressive strength, "
            "and fineness requirements."
        ),
    },
    {
        "id": "IS 8112: 1989",
        "title": "Specification for 43 Grade Ordinary Portland Cement",
        "category": "Cement",
        "keywords": [
            "ordinary portland cement", "opc", "43 grade", "43grade",
            "high strength cement", "structural concrete cement",
            "portland cement 43"
        ],
        "description": (
            "Specifies requirements for 43 Grade OPC, used in structural "
            "concrete, prestressed concrete, and high-strength applications. "
            "Higher compressive strength than IS 269. Covers chemical and "
            "physical tests including 28-day strength ≥43 MPa."
        ),
    },
    {
        "id": "IS 12269: 1987",
        "title": "Specification for 53 Grade Ordinary Portland Cement",
        "category": "Cement",
        "keywords": [
            "ordinary portland cement", "opc", "53 grade", "53grade",
            "high performance cement", "rcc cement", "rapid strength cement",
            "portland cement 53"
        ],
        "description": (
            "Specifies 53 Grade OPC for high-performance concrete, prestressed "
            "concrete, and fast-track construction. 28-day strength ≥53 MPa. "
            "Covers chemical limits, fineness, setting time, and soundness."
        ),
    },
    {
        "id": "IS 455: 1989",
        "title": "Specification for Portland Slag Cement",
        "category": "Cement",
        "keywords": [
            "portland slag cement", "psc", "blast furnace slag", "slag cement",
            "ground granulated blast furnace slag", "ggbs", "ggbfs",
            "sulphate resisting", "chemical plant cement", "marine cement",
            "slag blended cement", "manufacture portland slag"
        ],
        "description": (
            "Covers manufacture, chemical composition, and physical requirements "
            "for Portland Slag Cement made by intimately mixing OPC clinker, "
            "gypsum, and granulated slag. Suitable for marine structures, "
            "structures in sulphate-bearing soils, and general construction. "
            "Slag content: 25–65% by mass."
        ),
    },
    {
        "id": "IS 1489 (Part 1): 1991",
        "title": "Specification for Portland Pozzolana Cement — Fly Ash Based",
        "category": "Cement",
        "keywords": [
            "portland pozzolana cement", "ppc", "fly ash", "flyash",
            "pozzolana cement fly ash", "blended cement fly ash",
            "thermal power plant waste cement"
        ],
        "description": (
            "Specifies Portland Pozzolana Cement made with fly ash as pozzolanic "
            "material. Fly ash content: 15–35%. Used in mass concrete, marine "
            "works, and general construction. Lower heat of hydration than OPC."
        ),
    },
    {
        "id": "IS 1489 (Part 2): 1991",
        "title": "Specification for Portland Pozzolana Cement — Calcined Clay Based",
        "category": "Cement",
        "keywords": [
            "portland pozzolana cement", "ppc", "calcined clay", "metakaolin",
            "pozzolana cement clay", "blended cement clay", "calcined clay cement",
            "clay based pozzolana", "setting up plant pozzolana"
        ],
        "description": (
            "Covers Portland Pozzolana Cement manufactured using calcined clay "
            "(like metakaolin) as the pozzolanic material instead of fly ash. "
            "Calcined clay content: 15–35%. Suitable for hydraulic structures "
            "and general construction."
        ),
    },
    {
        "id": "IS 8041: 1990",
        "title": "Specification for Rapid Hardening Portland Cement",
        "category": "Cement",
        "keywords": [
            "rapid hardening cement", "rhpc", "fast setting cement",
            "early strength cement", "quick strength cement",
            "cold weather concreting cement"
        ],
        "description": (
            "Specifies Rapid Hardening Portland Cement, achieving high early "
            "strength — 3-day strength equivalent to 7-day OPC strength. "
            "Used for formwork removal, cold weather concreting, and repairs."
        ),
    },
    {
        "id": "IS 8043: 1991",
        "title": "Specification for Hydrophobic Portland Cement",
        "category": "Cement",
        "keywords": [
            "hydrophobic cement", "water repellent cement", "storage cement",
            "humid climate cement", "deterioration resistant cement"
        ],
        "description": (
            "Specifies Hydrophobic Portland Cement, which contains water-repellent "
            "additives to prevent deterioration during storage in humid conditions. "
            "Properties similar to OPC once mixed with water."
        ),
    },
    {
        "id": "IS 6452: 1989",
        "title": "Specification for High Alumina Cement for Structural Use",
        "category": "Cement",
        "keywords": [
            "high alumina cement", "hac", "calcium aluminate cement",
            "refractory cement", "chemical resistant cement",
            "alumina cement structural"
        ],
        "description": (
            "Covers High Alumina Cement (calcium aluminate cement) for structural "
            "use where resistance to chemical attack, high temperatures, or "
            "very rapid strength gain is required."
        ),
    },
    {
        "id": "IS 6909: 1990",
        "title": "Specification for Supersulphated Cement",
        "category": "Cement",
        "keywords": [
            "supersulphated cement", "sulphate resistant", "marine works",
            "aggressive water", "acidic soil cement", "chemical resistant cement",
            "supersulfated", "highly sulphate bearing"
        ],
        "description": (
            "Specifies Supersulphated Cement made from granulated slag, calcium "
            "sulphate, and a small amount of Portland cement clinker. Excellent "
            "resistance to sulphate attack, seawater, and aggressive water. "
            "Ideal for marine works, sewage structures, and chemical plants."
        ),
    },
    {
        "id": "IS 8042: 1989",
        "title": "Specification for White Portland Cement",
        "category": "Cement",
        "keywords": [
            "white portland cement", "white cement", "decorative cement",
            "architectural cement", "aesthetic cement", "white finish",
            "ornamental concrete", "terrazzo cement"
        ],
        "description": (
            "Covers White Portland Cement for architectural and decorative purposes "
            "such as terrazzo floors, exposed concrete, precast ornamental units, "
            "and white or coloured mortars/renders. Low iron oxide content gives "
            "white colour. Specifies whiteness, chemical, and physical requirements."
        ),
    },
    {
        "id": "IS 3466: 1988",
        "title": "Specification for Masonry Cement",
        "category": "Cement",
        "keywords": [
            "masonry cement", "mortar cement", "brick mortar cement",
            "plastering cement", "general purpose mortar",
            "non-structural mortar cement", "masonry work cement",
            "pointing mortar cement"
        ],
        "description": (
            "Specifies Masonry Cement for preparing mortar used in masonry, "
            "plastering, and pointing. NOT intended for structural concrete. "
            "Contains plasticisers or inert fillers blended with Portland cement "
            "for improved workability. Covers workability, strength, and soundness."
        ),
    },
    {
        "id": "IS 12330: 1988",
        "title": "Specification for Sulphate Resisting Portland Cement",
        "category": "Cement",
        "keywords": [
            "sulphate resisting cement", "src", "sulfate resistant",
            "foundation cement sulphate soil", "chemical resistance cement",
            "saline soil cement"
        ],
        "description": (
            "Specifies Sulphate Resisting Portland Cement (SRPC) for use in "
            "foundations, sewers, and structures exposed to sulphate soils or "
            "water. Low C3A content limits sulphate reaction."
        ),
    },

    # ─── AGGREGATES ────────────────────────────────────────────────────────────
    {
        "id": "IS 383: 1970",
        "title": "Specification for Coarse and Fine Aggregates from Natural Sources for Concrete",
        "category": "Aggregates",
        "keywords": [
            "coarse aggregate", "fine aggregate", "natural aggregate", "sand",
            "gravel", "crushed stone", "concrete aggregate", "structural concrete",
            "aggregate grading", "sieve analysis aggregate", "aggregate quality"
        ],
        "description": (
            "Specifies quality, grading, and testing requirements for coarse and "
            "fine aggregates from natural sources for use in concrete construction. "
            "Covers grading limits, deleterious materials, organic impurities, "
            "soundness, flakiness index, and sieve analysis for all zones of sand."
        ),
    },
    {
        "id": "IS 2116: 1980",
        "title": "Specification for Sand for Masonry Mortars",
        "category": "Aggregates",
        "keywords": [
            "masonry sand", "mortar sand", "bricklaying sand",
            "plastering sand", "sand masonry", "sand mortar"
        ],
        "description": (
            "Specifies requirements for sand (fine aggregate) used in masonry "
            "mortars for brickwork, blockwork, and plastering. Covers grading, "
            "clay content, organic impurities, and silt content."
        ),
    },
    {
        "id": "IS 9142: 1979",
        "title": "Specification for Artificial Lightweight Aggregates for Concrete Masonry Units",
        "category": "Aggregates",
        "keywords": [
            "lightweight aggregate", "artificial aggregate", "expanded clay",
            "sintered fly ash", "lightweight concrete block aggregate",
            "leca", "aerated aggregate"
        ],
        "description": (
            "Covers artificial lightweight aggregates (expanded clay, shale, slate, "
            "sintered fly ash) for use in concrete masonry units. Specifies bulk "
            "density, strength, and grading for structural and non-structural use."
        ),
    },

    # ─── CONCRETE PIPES ────────────────────────────────────────────────────────
    {
        "id": "IS 458: 2003",
        "title": "Specification for Precast Concrete Pipes (with and without Reinforcement)",
        "category": "Concrete Products",
        "keywords": [
            "precast concrete pipe", "rcc pipe", "water main pipe",
            "drainage pipe concrete", "reinforced concrete pipe",
            "non reinforced concrete pipe", "sewerage pipe concrete",
            "culvert pipe", "concrete pipe water"
        ],
        "description": (
            "Specifies dimensions, materials, workmanship, and testing for precast "
            "concrete pipes, both unreinforced and reinforced, for use as water "
            "mains, sewers, drains, and culverts. Covers crushing strength, "
            "hydrostatic test, absorption, and permissible loads."
        ),
    },
    {
        "id": "IS 4996: 1984",
        "title": "Specification for Vibrated Concrete Pipes (with and without Steel Cylinder)",
        "category": "Concrete Products",
        "keywords": [
            "vibrated concrete pipe", "prestressed concrete pipe",
            "pressure pipe", "water transmission pipe concrete",
            "steel cylinder pipe"
        ],
        "description": (
            "Covers vibrated concrete pressure pipes with and without steel cylinder "
            "for water transmission under pressure. Specifies manufacturing, testing, "
            "and pressure ratings."
        ),
    },
    {
        "id": "IS 12592: 2002",
        "title": "Specification for Precast Concrete Manhole Cover and Frame",
        "category": "Concrete Products",
        "keywords": [
            "manhole cover concrete", "precast manhole", "drain cover concrete",
            "inspection cover concrete"
        ],
        "description": (
            "Specifies requirements for precast concrete manhole covers and frames "
            "for drainage and sewerage systems."
        ),
    },

    # ─── CONCRETE BLOCKS / MASONRY ─────────────────────────────────────────────
    {
        "id": "IS 2185 (Part 1): 1979",
        "title": "Specification for Concrete Masonry Units — Hollow and Solid Concrete Blocks",
        "category": "Masonry",
        "keywords": [
            "concrete block", "hollow concrete block", "solid concrete block",
            "concrete masonry unit", "cmu", "load bearing block",
            "partition block concrete", "dense concrete block"
        ],
        "description": (
            "Specifies dimensions, compressive strength, water absorption, and "
            "drying shrinkage for hollow and solid dense concrete masonry blocks. "
            "Covers load-bearing and non-load-bearing blocks for walls and partitions."
        ),
    },
    {
        "id": "IS 2185 (Part 2): 1983",
        "title": "Specification for Concrete Masonry Units — Hollow and Solid Lightweight Concrete Blocks",
        "category": "Masonry",
        "keywords": [
            "lightweight concrete block", "lightweight hollow block",
            "lightweight solid block", "lightweight masonry block",
            "lightweight concrete masonry unit", "low density block",
            "thermal insulation block", "aerated concrete block masonry"
        ],
        "description": (
            "Specifies dimensions, physical requirements, and testing for hollow "
            "and solid lightweight concrete masonry blocks (using lightweight "
            "aggregates). Covers density classes, compressive strength, water "
            "absorption, and drying shrinkage. Ideal for reducing structural load."
        ),
    },
    {
        "id": "IS 2185 (Part 3): 1984",
        "title": "Specification for Concrete Masonry Units — Aerated Concrete Blocks",
        "category": "Masonry",
        "keywords": [
            "aerated concrete block", "autoclaved aerated concrete", "aac block",
            "cellular concrete block", "foam concrete block",
            "gas concrete block", "aac masonry"
        ],
        "description": (
            "Specifies Autoclaved Aerated Concrete (AAC) blocks. Covers density, "
            "compressive strength, drying shrinkage, and thermal conductivity. "
            "Very light weight, good thermal and acoustic insulation."
        ),
    },
    {
        "id": "IS 9893: 1981",
        "title": "Specification for Precast Concrete Lintels",
        "category": "Masonry",
        "keywords": [
            "precast lintel", "concrete lintel", "window lintel",
            "door lintel", "rcc lintel precast"
        ],
        "description": (
            "Specifies requirements for precast concrete lintels for use over "
            "openings in masonry walls. Covers dimensions, reinforcement, "
            "and strength."
        ),
    },
    {
        "id": "IS 12440: 1988",
        "title": "Specification for Precast Concrete Stone Masonry Blocks",
        "category": "Masonry",
        "keywords": [
            "stone masonry block", "precast stone block",
            "imitation stone block", "architectural block"
        ],
        "description": (
            "Covers precast concrete blocks simulating natural stone for architectural "
            "and general masonry use."
        ),
    },

    # ─── BRICKS ────────────────────────────────────────────────────────────────
    {
        "id": "IS 1077: 1992",
        "title": "Specification for Common Burnt Clay Building Bricks",
        "category": "Bricks",
        "keywords": [
            "burnt clay brick", "red brick", "building brick",
            "common brick", "clay brick", "fired brick",
            "masonry brick", "kiln brick"
        ],
        "description": (
            "Specifies dimensions, compressive strength, water absorption, and "
            "efflorescence for common burnt clay bricks used in buildings. "
            "Covers classes from Class 3.5 to Class 35."
        ),
    },
    {
        "id": "IS 2222: 1979",
        "title": "Specification for Burnt Clay Perforated Building Bricks",
        "category": "Bricks",
        "keywords": [
            "perforated brick", "hollow brick clay", "perforated clay brick",
            "lightweight clay brick", "holed brick"
        ],
        "description": (
            "Specifies perforated burnt clay bricks with holes through the thickness, "
            "offering reduced weight and improved thermal properties."
        ),
    },
    {
        "id": "IS 3952: 1988",
        "title": "Specification for Burnt Clay Hollow Blocks for Walls and Partitions",
        "category": "Bricks",
        "keywords": [
            "hollow clay block", "clay hollow block", "burnt clay hollow block",
            "partition wall block clay", "hollow terracotta block"
        ],
        "description": (
            "Specifies burnt clay hollow blocks for load-bearing and non-load-bearing "
            "walls and partitions. Includes size, strength, and absorption requirements."
        ),
    },
    {
        "id": "IS 4139: 1989",
        "title": "Specification for Calcium Silicate (Sandlime and Flintlime) Bricks",
        "category": "Bricks",
        "keywords": [
            "calcium silicate brick", "sandlime brick", "flintlime brick",
            "sand lime brick", "autoclaved brick", "silicate brick"
        ],
        "description": (
            "Specifies calcium silicate bricks made from sand (or flint) and lime, "
            "cured under steam pressure. Smooth surface, uniform colour, "
            "and good dimensional accuracy."
        ),
    },
    {
        "id": "IS 2691: 1988",
        "title": "Specification for Burnt Clay Facing Bricks",
        "category": "Bricks",
        "keywords": [
            "facing brick", "architectural brick", "decorative brick",
            "exposed brick", "clay facing brick", "aesthetic brick"
        ],
        "description": (
            "Specifies facing bricks of burnt clay for exposed surfaces requiring "
            "uniform appearance and colour. Higher dimensional tolerance and "
            "surface finish than common bricks."
        ),
    },

    # ─── ASBESTOS CEMENT / ROOFING ──────────────────────────────────────────────
    {
        "id": "IS 459: 1992",
        "title": "Specification for Corrugated and Semi-Corrugated Asbestos Cement Sheets",
        "category": "Roofing",
        "keywords": [
            "asbestos cement sheet", "corrugated sheet roofing",
            "semi-corrugated sheet", "ac sheet roofing", "asbestos roofing",
            "corrugated roofing sheet", "cladding sheet asbestos",
            "ac roofing corrugated"
        ],
        "description": (
            "Specifies corrugated and semi-corrugated asbestos cement sheets used "
            "for roofing and side cladding. Covers physical dimensions, mass, "
            "breaking load, water tightness, and load-bearing capacity."
        ),
    },
    {
        "id": "IS 1592: 2003",
        "title": "Specification for Asbestos Cement Pressure Pipes and Joints",
        "category": "Pipes",
        "keywords": [
            "asbestos cement pipe", "ac pipe", "asbestos pressure pipe",
            "water supply asbestos pipe", "ac pressure pipe"
        ],
        "description": (
            "Covers asbestos cement pressure pipes for conveyance of water. "
            "Specifies pressure classes, dimensions, strength, and testing."
        ),
    },
    {
        "id": "IS 6073: 1971",
        "title": "Specification for Asbestos Cement Flat Sheets",
        "category": "Roofing",
        "keywords": [
            "asbestos cement flat sheet", "ac flat sheet",
            "flat asbestos sheet", "partition board asbestos"
        ],
        "description": (
            "Specifies flat asbestos cement sheets for partitions, wall cladding, "
            "and general building purposes. Covers dimensions, weight, and testing."
        ),
    },
    {
        "id": "IS 10388: 1982",
        "title": "Specification for Asbestos Cement Accessories for Corrugated and Semi-Corrugated Sheets",
        "category": "Roofing",
        "keywords": [
            "asbestos cement accessories", "ridge cap", "barge board",
            "roofing accessories asbestos", "corrugated sheet accessories"
        ],
        "description": (
            "Specifies accessories such as ridge caps, barge boards, and ventilators "
            "made of asbestos cement for use with corrugated roofing sheets."
        ),
    },
    {
        "id": "IS 13990: 1994",
        "title": "Specification for GRP/FRP Corrugated Sheets for Roofing and Cladding",
        "category": "Roofing",
        "keywords": [
            "grp sheet", "frp sheet", "fibreglass roofing",
            "glass reinforced plastic sheet", "translucent sheet",
            "grp corrugated", "fibre reinforced plastic roofing"
        ],
        "description": (
            "Specifies Glass Reinforced Plastic (GRP/FRP) corrugated sheets for "
            "roofing and cladding. Covers light transmission, dimensions, and "
            "mechanical properties."
        ),
    },

    # ─── STEEL ─────────────────────────────────────────────────────────────────
    {
        "id": "IS 1786: 2008",
        "title": "Specification for High Strength Deformed Steel Bars and Wires for Concrete Reinforcement",
        "category": "Steel",
        "keywords": [
            "tmt bar", "deformed bar", "rebar", "reinforcement bar",
            "fe415", "fe500", "fe550", "fe600", "high strength deformed bar",
            "hsd bar", "thermo mechanically treated", "structural steel bar",
            "concrete reinforcement steel"
        ],
        "description": (
            "Specifies high strength deformed steel bars (TMT bars) grades Fe 415, "
            "Fe 500, Fe 550, Fe 600 for concrete reinforcement. Covers chemical "
            "composition, tensile properties, bend test, and dimensions. Most widely "
            "used standard for construction reinforcement in India."
        ),
    },
    {
        "id": "IS 2062: 2011",
        "title": "Hot Rolled Medium and High Tensile Structural Steel",
        "category": "Steel",
        "keywords": [
            "structural steel", "ms plate", "mild steel",
            "hot rolled steel", "structural fabrication steel",
            "e250", "e350", "e410", "medium tensile steel"
        ],
        "description": (
            "Specifies hot rolled medium and high tensile structural steel for "
            "general structural purposes including bridges, buildings, railway "
            "wagons, and ship building. Grades E 250 to E 650."
        ),
    },
    {
        "id": "IS 432 (Part 1): 1982",
        "title": "Specification for Mild Steel and Medium Tensile Steel Bars for Concrete Reinforcement",
        "category": "Steel",
        "keywords": [
            "mild steel bar", "ms bar", "plain bar reinforcement",
            "round bar concrete", "mild steel reinforcement"
        ],
        "description": (
            "Covers plain mild steel and medium tensile steel bars for concrete "
            "reinforcement. Grades Grade I and Grade II."
        ),
    },
    {
        "id": "IS 1566: 1982",
        "title": "Specification for Hard Drawn Steel Wire Fabric for Concrete Reinforcement",
        "category": "Steel",
        "keywords": [
            "steel wire fabric", "welded mesh", "wire mesh reinforcement",
            "hard drawn wire", "welded wire fabric"
        ],
        "description": (
            "Covers hard drawn steel wire and welded wire fabric used as "
            "reinforcement in concrete slabs, pipes, and precast units."
        ),
    },

    # ─── TILES ────────────────────────────────────────────────────────────────
    {
        "id": "IS 1237: 1980",
        "title": "Specification for Cement Concrete Flooring Tiles",
        "category": "Tiles",
        "keywords": [
            "cement tile", "floor tile", "concrete flooring tile",
            "mosaic tile", "colour tile", "plain tile flooring"
        ],
        "description": (
            "Specifies plain, chequered, and mosaic cement concrete flooring tiles. "
            "Covers transverse strength, water absorption, and wear resistance."
        ),
    },
    {
        "id": "IS 777: 1988",
        "title": "Specification for Glazed Earthenware Tiles",
        "category": "Tiles",
        "keywords": [
            "glazed tile", "ceramic tile", "earthenware tile",
            "wall tile", "bathroom tile", "kitchen tile"
        ],
        "description": (
            "Covers glazed earthenware tiles for wall and floor cladding. "
            "Specifies dimensions, glaze quality, water absorption, and crazing resistance."
        ),
    },
    {
        "id": "IS 15622: 2006",
        "title": "Specification for Ceramic/Vitrified Tiles",
        "category": "Tiles",
        "keywords": [
            "vitrified tile", "ceramic tile", "porcelain tile",
            "polished tile", "vitrified floor tile"
        ],
        "description": (
            "Specifies ceramic and vitrified tiles (including porcelain) for floors "
            "and walls. Covers dimensions, breaking strength, slip resistance, "
            "and chemical resistance."
        ),
    },

    # ─── GYPSUM / PLASTER ──────────────────────────────────────────────────────
    {
        "id": "IS 2547 (Part 1): 1976",
        "title": "Specification for Gypsum Building Plaster — Un-calcined Gypsum",
        "category": "Plaster",
        "keywords": [
            "gypsum plaster", "plaster of paris", "gypsum board",
            "gypsum building plaster", "ceiling plaster gypsum"
        ],
        "description": (
            "Specifies gypsum-based building plasters for interior plastering, "
            "ornamental work, and ceiling finishes."
        ),
    },

    # ─── WATER PROOFING ────────────────────────────────────────────────────────
    {
        "id": "IS 1322: 1993",
        "title": "Specification for Bitumen Felts for Waterproofing and Damp-Proofing",
        "category": "Waterproofing",
        "keywords": [
            "bitumen felt", "waterproofing membrane", "damp proofing",
            "bituminous felt", "roof waterproofing", "dpc membrane"
        ],
        "description": (
            "Specifies bitumen felt for waterproofing roofs and damp-proofing "
            "foundations. Covers grades, breaking strength, and water permeability."
        ),
    },

    # ─── GLASS ────────────────────────────────────────────────────────────────
    {
        "id": "IS 2835: 1987",
        "title": "Specification for Flat Transparent Sheet Glass",
        "category": "Glass",
        "keywords": [
            "flat glass", "sheet glass", "window glass",
            "transparent glass", "clear glass"
        ],
        "description": (
            "Specifies flat transparent (clear) sheet glass for windows, doors, "
            "and glazing. Covers thickness, tolerances, and optical quality."
        ),
    },

    # ─── LIME ─────────────────────────────────────────────────────────────────
    {
        "id": "IS 712: 1984",
        "title": "Specification for Building Limes",
        "category": "Lime",
        "keywords": [
            "building lime", "hydraulic lime", "fat lime",
            "hydrated lime", "quicklime", "lime mortar", "whitewash lime"
        ],
        "description": (
            "Specifies building limes — fat lime, hydraulic lime, and dolomite lime "
            "— used in mortar, plaster, and whitewash. Covers available CaO+MgO, "
            "residue, and CO2 content."
        ),
    },

    # ─── WOOD / TIMBER ────────────────────────────────────────────────────────
    {
        "id": "IS 4990: 1993",
        "title": "Specification for Plywood for Concrete Shuttering Work",
        "category": "Wood",
        "keywords": [
            "shuttering plywood", "formwork plywood", "concrete shuttering",
            "plywood formwork", "form plywood"
        ],
        "description": (
            "Specifies plywood panels used as shuttering (formwork) for concrete. "
            "Covers bending strength, glue bond, moisture resistance, and reuse cycles."
        ),
    },
]

# Build a quick-lookup dict by ID
STANDARDS_BY_ID = {s["id"]: s for s in BIS_STANDARDS}
