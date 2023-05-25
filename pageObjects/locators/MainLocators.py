class MainLocators:
    SMART_BAR = '//*[@data-purpose="smart-bar"]'
    SMART_BAR_BUTTON = '//*[@data-purpose="smart-bar-hide"]'

    LOGO = '//*[@class="header--flex-middle--2QeVR header--logo--rd7-H"]'

    CATEGORIES = '//*[@class="popper-module--popper--2BpLn header--gap-button--1p5bX"]'
    SUB_CATEGORIES = '//*[@class="js-browse-nav-level-one browse-nav--nav--1ssWv"]'

    SEARCH_INPUT = '//*[@data-testid="search-input"]'

    UDEMY_BUSINESS = '//*[@class="popper-module--popper--2BpLn header--gap-button--1p5bX header--group-a--3BELn"]'
    BUSINESS_MODAL_WINDOW = '//*[@data-purpose="hook-text"]'
    TRY_UDEMY_BUSINESS = '//*[@data-purpose="try-ufb-button"]'

    TEACH_ON_UDEMY = '//*[@id="u78-popper-trigger--10"]'

    BASKET = '//*[@id="udemy"]//div[4]/div[5]'
    LOG_IN = '//*[@data-purpose="header-login"]'
    SIGN_UP = '//*[@data-purpose="header-signup"]'

    CHOOSE_A_LANGUAGE = '//*[@id="udemy"]//div[8]/button'

    DEVELOPER_BUTTON = '//*[@data-id="288"]'

    PRIVACY = '//*[@id="onetrust-banner-sdk"]'
    ACCEPT_PRIVACY = '//*[@id="accept-recommended-btn-handler"]'
    MAIN_BANNER = '//*[@class="billboard-banner--image-container--3lMr5"]'

    SKILLS_HUB = '//*[@data-purpose="skills-hub-unit"]'
    FIRST_BUTTON_IN_SKILLS_HUB = '//*[@id="u47-tabs--2-tab-0"]'
    SECOND_BUTTON_IN_SKILLS_HUB = (
        '//*[contains(@class,"tabs-module--nav-button-container--u4wUp")]'
    )

    HEAD_SHOT_TEXT_SKILL_HUB = (
        '//*[@class="ud-heading-xl headshot-banner--tagline--25noN"]'
    )
    SECOND_HEAD_SHOT_TEXT_SKILL_HUB = (
        '//*[@id="u47-tabs--2-content-0"]/div/div[1]/div/h2'
    )

    TITLE_PYTHON = "Expand your career opportunities with Python"
    TITLE_EXCEL = "Analyze and visualize data with Excel"
