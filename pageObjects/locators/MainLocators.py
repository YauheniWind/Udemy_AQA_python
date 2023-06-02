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

    TEACH_ON_UDEMY = '//*[@data-purpose="instructor-dropdown"]'
    TEACH_MODAL_WINDOW = '//*[@class="ud-heading-lg panel-menu--gap-bottom--iiRgE"]'
    LEARN_MORE = '//*[@href="/teaching/?ref=teach_header"]'
    BLOCK_TEACH = '//*[@class="popper-module--popper-content--3cLBV header--dropdown--2qg7Q"]'

    BASKET_CART = '//*[@data-purpose="cart-icon"]'
    BASKET_MODAL_WINDOW = '//*[@class="ud-text-md panel-menu--gap-bottom--iiRgE panel-menu--no-items--2oxzC"]'
    BASKET_EMPTY_TITLE = 'Your cart is empty.'

    ADD_TO_BASKET = '//*[@data-testid="add-to-cart-button"]'
    CLOSE_POP_UP = '//*[@data-purpose="close-popup"]'
    PRODUCT_INFO_IN_BASKET = '//*[@class="ud-heading-sm shopping-item--buyable-title--1akia ud-focus-visible-target item-card-module--item-card-title--S729p"]'
    NAME_OF_PRODUCT = 'The Complete Python Bootcamp From Zero to Hero in Python'

    BANNER_ABOVE_HEADER = '//*[@data-purpose="smart-bar-container"]'
    CLOSE_BANNER_ABOVE_HEADER = '//*[@data-purpose="smart-bar-hide"]'

    LOG_IN = '//*[@data-purpose="header-login"]'
    SIGN_UP = '//*[@data-purpose="header-signup"]'

    CHOOSE_A_LANGUAGE = '//*[@id="udemy"]//div[8]/button'
    RUSSIAN_LANGUAGE = '//*[@lang="ru"]'
    CHANGED_LANGUAGE_BANNER = '//*[@id="Большой выбор курсов"]'
    TITLE_IN_RUSSIAN = "Большой выбор курсов"

    DEVELOPER_BUTTON = '//*[@data-id="288"]'

    PRIVACY = '//*[@id="onetrust-banner-sdk"]'
    ACCEPT_PRIVACY = '//*[@id="accept-recommended-btn-handler"]'

    MAIN_BANNER = '//*[@class="carousel-billboard--carousel-billboard-container--5hTpo"]'

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

    EXPLORE_PYTHON = '//*[@id="u33-tabs--2-content-0"]/div/div[1]/a/span'
    HOW_LEARN_TITLE = '//*[@class="ud-heading-xl"]'

    ARROW_NEXT = '//*[@data-pager-type="next"]'
    CART = '//*[@href="/course/complete-python-bootcamp/"]'

    CART_ON_MAIN_PAGE = '//*[@data-purpose="course-details-popover-trigger"]'
    TITLE_MODAL_WINDOW_CART = '//*[@data-purpose="quick-view-box-title"]'
    ADD_TO_CART_BUTTON = '//*[@data-testid="add-to-cart-button"]'
    ADD_TO_WISH_LIST_BUTTON = '//*[@class="course-details-quick-view-box--wishlist--1DehW"]'

    HOW_LEARN_SECTION = '//*[@class="ud-container discovery-units--testimonials--1ErIi"]'
    STUDENTS = '//*[@data-purpose="discovery-unit-1152523765"]'
    NEXT_BUTTON_HOW_LEARN = '//*[@id="udemy"]//section/div[2]/button[2]'
    STUDENTS_NAME = '//*[@data-purpose="user-name"]'

    COMMENT_IN_HOW_LEARN = '//*[@class="testimonial-card--testimonial--1vJ4Y"]'
    NAME_OF_COURSE_IN_HOW_LEARN = '//*[@class="ud-btn ud-btn-large ud-btn-link ud-heading-md"]'

